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
    search=request.args.get('search','').strip()
    if search:
        lots=ParkingLot.query.filter(ParkingLot.name.ilike(f'%{search}%') | ParkingLot.address.ilike(f'%{search}%')).all()
    
    
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
        model=request.form.get('model').title()
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


    
@user_bp.route('/user/charts')
@login_required
@user_required
def user_charts():
    user=User.query.get(session.get('user_id'))
    history=History.query.filter_by(user_id=user.id).all()
    regular_spot=0
    ev_spot=0
    total_time=0
    booking_per_month_dict={}
    lot_parking_dict={}
    revenue_dict={}
    for h in history:
        month = h.exit_time.strftime('%m')
        booking_per_month_dict[month]=booking_per_month_dict.get(month,0)+1
        lot=ParkingLot.query.get(h.lot_id)
        lot_parking_dict[lot.name]=lot_parking_dict.get(lot.name,0)+1
        revenue_dict[month]=revenue_dict.get(month,0)+h.total_amount_paid
        total_time+=h.duration
        if h.is_ev_spot:
            ev_spot+=1
        else:
            regular_spot+=1
    
    month_names= ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    revenue_lst=[0]*12
    spendings_lst=list(revenue_dict.values())
    month_num=list(booking_per_month_dict.keys())
    bookings_num=list(booking_per_month_dict.values())
    booking_month_lst=[0]*12
    for i in range(len(month_num)):
        booking_month_lst[int(month_num[i])]=bookings_num[i]
        revenue_lst[int(month_num[i])]=spendings_lst[i]
        
    # chart-1
     
    chart1_labels=month_names
    chart1_data=booking_month_lst
    top_month=chart1_labels[chart1_data.index(max(chart1_data))]
    
    
    # chart-2
    
    chart2_labels=list(lot_parking_dict.keys())
    chart2_data=list(lot_parking_dict.values())
    
    top_lot=chart2_labels[chart2_data.index(max(chart2_data))] if chart2_data else 'NA'
    
    # chart-3
    chart3_labels=['Regular Spot','Ev Spot']
    chart3_data=[regular_spot,ev_spot]
    
    # chart-4
    chart4_labels=month_names
    chart4_data=revenue_lst
    avg_spendings=round(sum(revenue_lst)/12,2)
    
    
    
    return render_template('user_charts.html',user=user,chart1_labels=chart1_labels,chart1_data=chart1_data,chart2_labels=chart2_labels,chart2_data=chart2_data,chart3_labels=chart3_labels,chart3_data=chart3_data,chart4_labels=chart4_labels,chart4_data=chart4_data,avg_spendings=avg_spendings,top_lot=top_lot,top_month=top_month,total_time=int(total_time))
