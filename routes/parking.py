from flask import Blueprint,render_template,request,redirect,url_for,session,flash

from models import ParkingLot
from config import db
parking_bp = Blueprint('parking', __name__)

@parking_bp.route('/parking_dashboard', methods=['GET', 'POST'])
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
            flash('Please fill in all required fields')
            return redirect(url_for('parking.parking_dashboard'))
        if not is_24_hours:
            if not opening_time or not closing_time:
                flash('Please fill in all required fields')
                return redirect(url_for('parking.parking_dashboard'))
        
        new_parking_lot = ParkingLot(
            name=pl_name,
            address=address,
            pincode=pincode,
            hourly_rate=hourly_rate,
            total_spots=total_spots,
            ev_spots=ev_spots,
            ev_charging_rate=ev_charging_rate,
            is_24_hours=is_24_hours,
            opening_time=opening_time if not is_24_hours else None,
            closing_time=closing_time if not is_24_hours else None,
            description=description
        )
        db.session.add(new_parking_lot)
        db.session.commit()
        print('hello')
        flash('Parking lot added successfully!')
        
    return redirect(url_for('admin.admin_dashboard'))
    
    

