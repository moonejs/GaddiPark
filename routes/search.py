from flask import Blueprint,render_template,request,redirect,url_for,session
from routes.decorators import login_required,admin_required
from models import ParkingLot,User,ParkingSpot,Booking,History

search_bp=Blueprint('search',__name__)
@search_bp.route('/admin/lot/search')
@login_required
@admin_required
def admin_lot_search():
    search=request.args.get('search').strip().lower()
    search_filter=request.args.get('search_filter')
    
    if search_filter == 'name':
        lots=ParkingLot.query.filter(ParkingLot.name.ilike(f'%{search}%'))
        return render_template('admin_dashboard.html', lots=lots)
    return "hellpo"