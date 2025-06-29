from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle,Booking,ParkingSpot
from routes.decorators import login_required,user_required
from config import db
from datetime import datetime

from datetime import datetime
import pytz
import uuid

booking_bp=Blueprint('booking',__name__)


@booking_bp.route('/find_parking/booking<int:lot_id>',methods=['POST','GET'])
@login_required
@user_required
def booking(lot_id):
    def generate_transaction_id():
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S") 
        random_part = uuid.uuid4().hex[:6].upper() 
        return f"TXN{timestamp}{random_part}"  
    
    lot=ParkingLot.query.get(lot_id)
    user=User.query.get(session.get('user_id'))
    wallet_balance=user.wallet_balance
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    current_booking_date = now.strftime("%d-%m-%Y") 
    current_booking_time = now.strftime("%I:%M %p")
    payment_method='None'
    if request.method=='POST':
        vehicle_id=request.form.get('vehicle')
        duration=request.form.get('duration')
        amount=float(request.form.get('estimate_cost'))
        payment_method=request.form.get('payment_method')
        
        if not vehicle_id or not duration or not amount or not payment_method:
            flash("Please fill in all booking details before confirming.")
            return redirect(url_for('user.find_parking', lot_id=lot_id, current_booking_time=current_booking_time, current_booking_date=current_booking_date, wallet_balance=wallet_balance))
        
        datetime_string = f"{current_booking_date} {current_booking_time}"
        start_time = datetime.strptime(datetime_string, "%d-%m-%Y %I:%M %p")

        booking_date = datetime.strptime(current_booking_date, "%d-%m-%Y").date()

        vehicle=Vehicle.query.get(vehicle_id)
        is_ev=vehicle.is_ev
        spot_id=None
        def findSpotId(lot_id,is_ev):
            spot=ParkingSpot.query.filter_by(lot_id=lot_id,is_ev_spot=is_ev,status='available').first()
            return spot.id
        
        spot_id=findSpotId(lot.id,is_ev)
        if not spot_id:
            flash("No available spot for your vehicle type")
            return redirect(url_for('user.find_parking', lot_id=lot_id, current_booking_time=current_booking_time,current_booking_date=current_booking_date,wallet_balance=wallet_balance))
           
        
        new_booking=Booking(user_id=user.id,vehicle_id=vehicle_id,lot_id=lot.id,spot_id=spot_id,duration=duration,date=booking_date,start_time=start_time,amount=amount)
        db.session.add(new_booking)
        db.session.commit()
        
        flash("Booking successful!")
        return render_template('booking_confirmed.html')
        
    return redirect(url_for('user.find_parking', lot_id=lot_id, current_booking_time=current_booking_time,current_booking_date=current_booking_date,wallet_balance=wallet_balance))