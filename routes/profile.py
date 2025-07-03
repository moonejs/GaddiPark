from flask import Blueprint, render_template, request, redirect, url_for, session,flash
from routes.decorators import login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from config import db

profile_bp =Blueprint('profile',__name__)

@profile_bp.route('/profile')
@login_required
def profile():
    user = User.query.get(session.get('user_id'))
    
    return render_template('profile.html', name=user.full_name, username=user.username,is_admin=user.is_admin,wallet_balance=user.wallet_balance)


@profile_bp.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    
    new_full_name=request.form.get('name')
    new_username =request.form.get('username')
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_new_password = request.form.get('confirm_new_password')
    
    if not new_full_name or not new_username or not current_password:
        flash('Please fill in all required fields', 'error')
        return redirect(url_for('profile.profile'))
    
    
    user = User.query.get(session.get('user_id'))
    if check_password_hash(user.password_hash,current_password):
        if new_password == confirm_new_password:
            if User.query.filter_by(username=new_username).first() and new_username != user.username:
                flash('Username already exists.', 'error')
                return redirect(url_for('profile.profile'))
            else:
                user.full_name=new_full_name
                user.username= new_username
                user.password_hash =generate_password_hash(new_password)
                db.session.commit()
        else:
            flash('New passwords do not match', 'error')
            return redirect(url_for('profile.profile'))
        flash('Profile updated successfully', 'success')
        return redirect(url_for('profile.profile'))
    else:
        flash('Current password is incorrect', 'error')
        return redirect(url_for('profile.profile'))