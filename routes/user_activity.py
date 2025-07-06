from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle,Booking,ParkingSpot
from routes.decorators import login_required,user_required
from config import db
import pytz
from datetime import datetime

user_activity_bp=Blueprint('user_activity',__name__)

@user_activity_bp.route('/confirm_booking')
@login_required
@user_required
def confirm_booking():
    booking_id=request.args.get('booking_id')
    booking=Booking.query.filter_by(booking_id=booking_id).first()
    spot=ParkingSpot.query.get(booking.spot_id)
    vehicle=Vehicle.query.get(booking.vehicle_id)
    lot=ParkingLot.query.get(booking.lot_id) 
    return render_template('booking_confirmed.html',booking=booking,spot=spot,vehicle=vehicle,lot=lot)

@user_activity_bp.route('/user_dashboard/current_booking')
@login_required
@user_required
def current_booking():
    
    booking_id = request.args.get('booking_id')
    user=User.query.get(session.get('user_id'))
    booking=Booking.query.filter_by(booking_id=booking_id).first()
    spot=ParkingSpot.query.get(booking.spot_id)
    vehicle=Vehicle.query.get(booking.vehicle_id)
    lot=ParkingLot.query.get(booking.lot_id)
    
    return render_template('user_dashboard.html',user=user,booking=booking,spot=spot,vehicle=vehicle,lot=lot)


@user_activity_bp.route('/release_spot',methods=['POST'])
@login_required
@user_required

def release_spot():
    user=User.query.get(session.get('user_id'))

    booking_id=request.form.get('booking_id')
    time = int(request.form.get('elapsed_minutes', 0))
    
    booking=Booking.query.filter_by(booking_id=booking_id).first()
    spot=ParkingSpot.query.get(booking.spot_id)
    vehicle=Vehicle.query.get(booking.vehicle_id)
    lot=ParkingLot.query.get(booking.lot_id)
    wallet_balance=user.wallet_balance
    
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    duration=int(booking.duration)
    normal_rate=lot.hourly_rate
    estimated_amount=duration*normal_rate
    if estimated_amount< booking.amount:
        total_amount=(normal_rate+lot.ev_charging_rate)*(time/60)
    else:
        total_amount=(normal_rate)*(time/60)
    
    total_duration=f'{time//60} hour {time%60} minutes' 
    
    current_leaving_time = now.strftime("%I:%M %p")
    
    return render_template('payment.html',heading="Pay for Parking",method="bank",lot=lot,spot=spot,booking=booking,total_amount=round(total_amount, 2),total_duration=total_duration,current_leaving_time=current_leaving_time,wallet_balance=user.wallet_balance,user=user)