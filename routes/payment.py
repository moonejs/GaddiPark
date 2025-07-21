from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle,Booking,ParkingSpot,Payment,History
from routes.decorators import login_required,user_required
from config import db
from datetime import datetime



from datetime import datetime
import pytz
import uuid

payment_bp=Blueprint('payment',__name__)

@payment_bp.route('/payment',methods=['POST'])
@login_required
@user_required
def payment():
    def generate_transaction_id():
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S") 
        random_part = uuid.uuid4().hex[:6].upper() 
        return f"TXN{timestamp}{random_part}" 
    
    payment_method=request.form.get('payment-method')
    total_amount_paid=float(request.form.get('total_amount_paid'))
    ist = pytz.timezone("Asia/Kolkata")
    payment_time = datetime.now(ist)
    
    user=User.query.get(session.get('user_id'))
    booking=Booking.query.filter_by(user_id=user.id).first()
    lot=ParkingLot.query.get(booking.lot_id)
    transaction_id=generate_transaction_id()
    spot=ParkingSpot.query.get(booking.spot_id)
    
    start_time=booking.start_time
    if start_time.tzinfo is None:
        start_time = ist.localize(start_time)
    duration_minutes = int((payment_time - start_time).total_seconds() // 60)
    
    if not payment_method:
        flash('Missing payment details or booking information.', 'error')
        return redirect(url_for('user.user_dashboard'))
    
    if payment_method =='wallet':
        if user.wallet_balance < total_amount_paid:
            flash('Insufficient wallet balance for this payment.', 'error')
            return redirect(url_for('user.user_dashboard'))
        else:
            user.wallet_balance -= total_amount_paid
            db.session.commit()
    elif payment_method not in ['card', 'UPI']: 
        flash('Invalid payment method selected.', 'error')
        return redirect(url_for('user.user_dashboard'))
    
    new_payment=Payment(booking_id=booking.booking_id,user_id=user.id,amount=total_amount_paid,payment_method=payment_method,transaction_id=transaction_id,payment_time=payment_time)
    
    new_history = History(user_id=user.id,lot_id=lot.id,spot_id=booking.spot_id,vehicle_id=booking.vehicle_id,booking_id=booking.booking_id,entry_time=start_time,exit_time=payment_time,total_amount_paid=total_amount_paid,
    payment_method=payment_method,transaction_id=transaction_id,duration=duration_minutes,is_ev_spot=spot.is_ev_spot
    )
    
    
    spot=ParkingSpot.query.get(booking.spot_id)
    spot.status='available'
    user.total_parkings += 1
    user.total_spendings+=round(total_amount_paid,2)
    db.session.add(new_payment)
    db.session.add(new_history)
    db.session.delete(booking)
    db.session.commit()
    
    regular_occupied_spots=ParkingSpot.query.filter_by(lot_id=lot.id,is_ev_spot=0,status='occupied').count()
    ev_occupied_spots=ParkingSpot.query.filter_by(lot_id=lot.id,is_ev_spot=1,status='occupied').count()

    lot.occupied_regular_spots=regular_occupied_spots
    lot.occupied_ev_spots=ev_occupied_spots
        
    db.session.commit()
    
    flash('Payment successful!', 'success')
    return redirect(url_for('payment.receipt',transaction_id=transaction_id))





@payment_bp.route('/receipt',methods=['POST','GET'])
@login_required
@user_required
def receipt():
    user=User.query.get(session.get('user_id'))
    transaction_id=request.args.get('transaction_id')
    history=History.query.filter_by(transaction_id=transaction_id).first()
    lot=ParkingLot.query.get(history.lot_id)
    spot=ParkingSpot.query.get(history.spot_id)
    vehicle=Vehicle.query.get(history.vehicle_id)
    return render_template('receipt.html',history=history,lot=lot,spot=spot,vehicle=vehicle)



@payment_bp.route('/payment/wallet',methods=['POST','GET'])
@login_required
@user_required  
def wallet_payment():
    user=User.query.get(session.get('user_id'))
    if request.method=='POST':
        amount=float(request.form.get('updated_wallet_balance'))
        payment_method=request.form.get('payment-method')
        if not amount or not payment_method:
            flash('All fields are required', 'error')
            return redirect(url_for('payment.wallet_payment'))
        if amount <= 0:
            flash('Please enter a valid amount to add', 'error')
            return redirect(url_for('payment.wallet_payment'))
        user.wallet_balance +=float(amount)
        db.session.commit()
        flash(f'₹{amount} added to your wallet successfully!', 'success')
        return redirect(url_for('user.user_dashboard'))
        
    
    return render_template('payment.html',method="wallet",heading="Add Money to Wallet",user=user)