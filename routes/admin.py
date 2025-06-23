from flask import Blueprint,render_template,request,redirect,url_for,session
from routes.decorators import login_required,admin_required
from models import ParkingLot

admin_bp=Blueprint('admin',__name__)

@admin_bp.route('/admin_dashboard')
@login_required
@admin_required
def admin_dashboard():
    plots=ParkingLot.query.all()
    plot_id=request.args.get('plot_id')
    plot = None
    if plot_id:
        plot=ParkingLot.query.filter_by(id=plot_id).first()
    
    return render_template('admin_dashboard.html',plots=plots,plot=plot)


