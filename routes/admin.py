from flask import Blueprint,render_template,request,redirect,url_for,session
from routes.decorators import login_required,admin_required
from models import ParkingLot

admin_bp=Blueprint('admin',__name__)

@admin_bp.route('/admin_dashboard')
@login_required
@admin_required
def admin_dashboard():
    lots=ParkingLot.query.all()
    lot_id=request.args.get('lot_id')
    lot = None
    if lot_id:
        lot=ParkingLot.query.filter_by(id=lot_id).first()
    
    return render_template('admin_dashboard.html',lots=lots,lot=lot)


