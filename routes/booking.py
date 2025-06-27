from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle
from routes.decorators import login_required,user_required
from config import db
from datetime import datetime

from datetime import datetime
import pytz

booking_bp=Blueprint('booking',__name__)


@booking_bp.route('/find_parking/booking<int:lot_id>',methods=['POST','GET'])
@login_required
@user_required
def booking(lot_id):
    lot=ParkingLot.query.get(lot_id)
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    current_booking_date = now.strftime("%d-%m-%Y") 
    current_booking_time = now.strftime("%I:%M %p")
    
    return redirect(url_for('user.find_parking', lot_id=lot_id, current_booking_time=current_booking_time,current_booking_date=current_booking_date))