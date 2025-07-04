from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from routes.decorators import login_required,admin_required

from datetime import timedelta

from models import ParkingLot,ParkingSpot,User,Vehicle,Booking
from config import db
parking_bp = Blueprint('parking', __name__)

@parking_bp.route('/parking_dashboard', methods=['GET', 'POST'])
@login_required
@admin_required
def parking_dashboard():
    if request.method == 'POST':
        pl_name=request.form.get('pl_name')
        address=request.form.get('address')
        pincode=request.form.get('pincode')
        hourly_rate = float(request.form.get('hourly_rate'))
        total_spots = int(request.form.get('total_spots'))
        ev_spots = int(request.form.get('ev_spots'))
        ev_charging_rate = float(request.form.get('ev_charging_rate'))

        is_24_hours=request.form.get('is_24_hours') =='1'
        opening_time = None
        closing_time = None
        if not is_24_hours:
            opening_time = request.form.get('opening_time')
            closing_time = request.form.get('closing_time')
        description = request.form.get('description')
        
        if not pl_name or not address or not pincode or not hourly_rate or not total_spots or not ev_spots or not ev_charging_rate:
            flash('Please fill in all required fields',"error")
            return redirect(url_for('parking.parking_dashboard'))
        if not is_24_hours:
            if not opening_time or not closing_time:
                flash('Please fill in all required fields',"error")
                return redirect(url_for('parking.parking_dashboard'))
            
        parking=ParkingLot.query.filter_by(name=pl_name).first()
        if parking:
            flash('Parking Lot name already Exist,please enter unique Lot name',"error")
            return redirect(url_for('parking.parking_dashboard'))
        
        
        new_parking_lot = ParkingLot(name=pl_name,address=address,pincode=pincode,hourly_rate=hourly_rate,total_spots=total_spots,ev_spots=ev_spots,ev_charging_rate=ev_charging_rate,is_24_hours=is_24_hours,opening_time=opening_time if not is_24_hours else None,closing_time=closing_time if not is_24_hours else None,description=description
        )
        db.session.add(new_parking_lot)
        db.session.commit()
        
        lot=ParkingLot.query.filter_by(name=pl_name).first()
        def add_spot(spots,type,is_e):
            n=0
            for s in range(1,spots+1):
                spot_number=f'{chr(65+n)}{type}{10 if s % 10 == 0 else s % 10}'
                new_parking_spot=ParkingSpot(lot_id=lot.id,spot_number=spot_number,is_ev_spot=is_e)
                db.session.add(new_parking_spot)
                db.session.commit()
                if s % 10 ==0:
                    n+=1
        add_spot(ev_spots,'E',1)
        add_spot(total_spots,'R',0)
        
        
        
        flash('Parking lot added successfully!',"success")
        
    return redirect(url_for('admin.admin_dashboard'))
    
    
@parking_bp.route('/update_lot<int:lot_id>',methods=['POST','GET'])
@login_required
@admin_required
def update_lot(lot_id):
    if request.method=='POST':
        lot=ParkingLot.query.get(lot_id)
        new_pl_name=request.form.get('pl_name')
        new_address=request.form.get('address')
        new_pincode=request.form.get('pincode')
        new_hourly_rate = float(request.form.get('hourly_rate'))
        new_ev_charging_rate = float(request.form.get('ev_charging_rate'))
        new_description = request.form.get('description')
        if not new_pl_name or not new_address or not new_pincode or not new_hourly_rate  or not new_ev_charging_rate or not new_description:
            flash('Please fill in all required fields')
            return redirect(url_for('parking.parking_dashboard'))
        parking=ParkingLot.query.filter_by(name=new_pl_name).first()
        if parking:
            flash('Parking Lot name already Exist,please enter unique Lot name')
            return redirect(url_for('parking.parking_dashboard'))
        
        lot.name=new_pl_name
        lot.address=new_address
        lot.pincode=new_pincode
        lot.hourly_rate=new_hourly_rate
        lot.ev_charging_rate=new_ev_charging_rate
        lot.description=new_description
        db.session.commit()
        
        flash('Parking Lot Successfully updated')
        return redirect(url_for('admin.admin_dashboard'))
    else:
        return redirect(url_for('admin.admin_dashboard'))
        


@parking_bp.route('/delete-lot<int:lot_id>')
@login_required
@admin_required
def delete_lot(lot_id):
    lot=ParkingLot.query.get(lot_id)
    if not (lot.occupied_regular_spots) and not (lot.occupied_ev_spots):
        db.session.delete(lot)
        db.session.commit()
        flash('Parking Lot deleted successfully!')
        return redirect(url_for('admin.admin_dashboard'))
    else:
        flash('Cannot delete parking lot: there are still occupied spots.')
        return redirect(url_for('admin.admin_dashboard'))
    

@parking_bp.route('/view_details',methods=['POST','GET'])
@login_required
@admin_required
def view_details():
    lot_id=request.args.get('lot_id')
    spot_id=request.args.get('spot_id')
    spot=ParkingSpot.query.get(spot_id)
    
    booking=Booking.query.filter_by(spot_id=spot_id).first()
    end_time=None
    user=None
    vehicle=None
    if booking:
        user=User.query.get(booking.user_id)
        vehicle=Vehicle.query.get(booking.vehicle_id)
        end_time=booking.start_time + timedelta(hours=booking.duration)
 
    if request.method=='POST':
        lot_id=request.form.get('lot_id')
        
    lot=ParkingLot.query.get(lot_id)
    spots=ParkingSpot.query.filter_by(lot_id=lot_id)
    
    return render_template('parking_lot_details.html',lot=lot,spots=spots,spot=spot,user=user,vehicle=vehicle,end_time=end_time,booking=booking)


@parking_bp.route('/view_details/spot_details',methods=['POST'])
@login_required
@admin_required
def spot_details():
    spot_id=request.form.get('spot_id')
    lot_id=request.form.get('lot_id')
        
    return redirect(url_for('parking.view_details',spot_id=spot_id,lot_id=lot_id))




@parking_bp.route('/view_details/spot_details/delete_spot',methods=['POST'])
@login_required
@admin_required
def delete_spot():
    spot_id=request.form.get('spot_id')
    spot=ParkingSpot.query.get(spot_id)
    lot=ParkingLot.query.get(spot.lot_id)
    db.session.delete(spot)
    db.session.commit()
    
    flash('Parking spot deleted successfully!', 'success')
    return redirect(url_for('parking.view_details', lot_id=lot.id))