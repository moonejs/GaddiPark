from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle,Booking,ParkingSpot
from routes.decorators import login_required,user_required
from config import db

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

