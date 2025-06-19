from flask import Blueprint, render_template, request, redirect, url_for, session
from routes.decorators import login_required

from models import User

profile_bp =Blueprint('profile',__name__)

@profile_bp.route('/profile')
@login_required
def profile():
    user = User.query.get(session.get('user_id'))
    
    return render_template('profile.html', name=user.full_name, username=user.username,is_admin=user.is_admin,wallet_balance=user.wallet_balance)
