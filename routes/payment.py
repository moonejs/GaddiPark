from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle,Booking,ParkingSpot,Payment
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
    total_amount_paid=request.form.get('total_amount_paid')
    ist = pytz.timezone("Asia/Kolkata")
    payment_time = datetime.now(ist)
    
    user=User.query.get(session.get('user_id'))
    booking=Booking.query.filter_by(user_id=user.id).first()
    transaction_id=generate_transaction_id()
    
    if not payment_method or not total_amount_paid or not booking:
        flash('Missing payment details or booking information.', 'error')
        return redirect(url_for('user.user_dashboard'))
    
    new_payment=Payment(booking_id=booking.booking_id,user_id=user.id,amount=total_amount_paid,payment_method=payment_method,transaction_id=transaction_id,payment_time=payment_time)
    
    
    spot=ParkingSpot.query.get(booking.spot_id)
    spot.status='available'
    db.session.add(new_payment)
    db.session.delete(booking)
    db.session.commit()
    
    flash('Payment successful! Thank you for your payment.')
    return redirect(url_for('user.user_dashboard'))
