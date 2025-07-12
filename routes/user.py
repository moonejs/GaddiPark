from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User ,ParkingLot,Vehicle,Booking,ParkingSpot,History
from routes.decorators import login_required,user_required
from config import db

user_bp=Blueprint('user',__name__)



@user_bp.route('/user_dashboard')
@login_required
@user_required
def user_dashboard():
    user=User.query.get(session.get('user_id'))
    booking=Booking.query.filter_by(user_id=user.id).first()
    user_history=History.query.filter_by(user_id=user.id).all()
    total_spending=0
    for i in user_history:
        total_spending+=i.total_amount_paid
    spot=None
    vehicle=None
    lot=None
    if booking:
        spot=ParkingSpot.query.get(booking.spot_id)
        vehicle=Vehicle.query.get(booking.vehicle_id)
        lot=ParkingLot.query.get(booking.lot_id)
    
    return render_template('user_dashboard.html',user=user,booking=booking,spot=spot,vehicle=vehicle,lot=lot,total_spending=total_spending)


        
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
    
    is_booked_by_user=Booking.query.filter_by(user_id=user.id).first()
    if is_booked_by_user:
        flash('You have any active bookings.', 'error')
        return redirect(url_for('user.user_dashboard'))
    
    lot = None

    if request.method == 'GET' and lot_id:
        lot = ParkingLot.query.filter_by(id=lot_id).first()

    
    return render_template('find_parking.html',lots=lots,lot=lot,vehicles=vehicles,current_booking_time=current_booking_time,current_booking_date=current_booking_date,user=user)




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
            flash('All fields are required.', 'error')
            return redirect(url_for('user.vehicle'))
        reg_num=Vehicle.query.filter_by(registration_number=registration_number).first()
        
        if reg_num:
            flash('Vehicle with this registration number already exists.', 'error')
            return redirect(url_for('user.vehicle'))
        
        new_vehicle=Vehicle(user_id=user.id,type=type,model=model,registration_number=registration_number,is_ev=is_ev)
        db.session.add(new_vehicle)
        db.session.commit()
        flash('Vehicle added successfully.', 'success')
        return redirect(url_for('user.vehicle'))
    
    else:
        vehicles=Vehicle.query.filter_by(user_id=user.id).all()
        return render_template('vehicle.html',vehicles=vehicles,user=user)
    
@user_bp.route('/vehicle/delete',methods=['POST'])
@login_required
@user_required
def vehicle_delete():
    user=User.query.get(session.get('user_id'))
    vehicle_id=request.form.get('vehicle_id')
    vehicle=Vehicle.query.get(vehicle_id)
    db.session.delete(vehicle)
    db.session.commit()
    flash('Vehicle deleted successfully.', 'success')
    return redirect(url_for('user.vehicle')) 