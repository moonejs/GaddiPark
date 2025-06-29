from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle
from routes.decorators import login_required,user_required
from config import db

user_bp=Blueprint('user',__name__)



@user_bp.route('/user_dashboard')
@login_required
@user_required
def user_dashboard():
    user=User.query.get(session.get('user_id'))
    return render_template('user_dashboard.html',user=user.full_name)


        
@user_bp.route('/find_parking',methods=['POST','GET'])
@login_required
@user_required
def find_parking():
    user=User.query.get(session.get('user_id'))
    vehicles=Vehicle.query.filter_by(user_id=user.id)
    lots=ParkingLot.query.all()
    lot_id=request.args.get('lot_id')
    current_booking_time= request.args.get('current_booking_time')
    current_booking_date= request.args.get('current_booking_date')
    wallet_balance=request.args.get('wallet_balance')
    lot = None
    if request.method == 'GET' and lot_id:
        lot = ParkingLot.query.filter_by(id=lot_id).first()

    
    return render_template('find_parking.html',lots=lots,lot=lot,vehicles=vehicles,current_booking_time=current_booking_time,current_booking_date=current_booking_date,wallet_balance=wallet_balance)




@user_bp.route('/vehicle',methods=['POST','GET'])
@login_required
@user_required
def vehicle():
    user=User.query.get(session.get('user_id')) 
    if request.method =='POST':
        type=request.form.get('type')
        model=request.form.get('model')
        registration_number=request.form.get('registration_number')
        is_ev=request.form.get('is_ev') =='1'
        
        if not type or not model or not registration_number or is_ev is None:
            flash('All fields are required.')
            return redirect(url_for('user.vehicle'))
        reg_num=Vehicle.query.filter_by(registration_number=registration_number).first()
        
        if reg_num:
            flash('Vehicle with this registration number already exists.')
            return redirect(url_for('user.vehicle'))
        
        new_vehicle=Vehicle(user_id=user.id,type=type,model=model,registration_number=registration_number,is_ev=is_ev)
        db.session.add(new_vehicle)
        db.session.commit()
        flash('Vehicle added successfully.')
        return redirect(url_for('user.vehicle'))
    
    else:
        vehicles=Vehicle.query.filter_by(user_id=user.id)
        return render_template('vehicle.html',vehicles=vehicles)