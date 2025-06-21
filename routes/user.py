from flask import Blueprint,render_template,request,redirect,url_for,session
from models import User
from routes.decorators import login_required,user_required

user_bp=Blueprint('user',__name__)



@user_bp.route('/user_dashboard')
@login_required
@user_required
def user_dashboard():
    user=User.query.get(session.get('user_id'))
    return render_template('user_dashboard.html',user=user.full_name)
        
