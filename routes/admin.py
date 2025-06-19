from flask import Blueprint,render_template,request,redirect,url_for,session
from routes.decorators import login_required
admin_bp=Blueprint('admin',__name__)

@admin_bp.route('/admin_dashboard')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')
