from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle,Booking,ParkingSpot
from routes.decorators import login_required,user_required
from config import db

payment_bp=Blueprint('payment',__name__)

@payment_bp.route('/payment')
@login_required
@user_required
def payment():
    heading=request.args.get('heading')
    method=request.args.get('method')
    amount=request.args.get('amount')
    
    return render_template('payment.html',heading=heading,method=method,amount=amount)
