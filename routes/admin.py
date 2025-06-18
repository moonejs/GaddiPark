from flask import Blueprint,render_template,request,redirect,url_for,session

admin_bp=Blueprint('admin',__name__)

@admin_bp.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    else :
        return render_template('admin_dashboard.html')