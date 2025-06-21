from functools import wraps
from flask import session, redirect, url_for, flash
from models import User

def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if 'user_id'  in session:
            return f(*args, **kwargs)
        else:
            flash('Please login to continue')
            return redirect(url_for('auth.login'))
    return inner

def admin_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        user = User.query.get(session.get('user_id'))
        if user and user.is_admin:
            return f(*args, **kwargs)
        else:
            flash('You do not have permission to access this page')
            return redirect(url_for('user.user_dashboard'))
    return inner 
def user_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        user = User.query.get(session.get('user_id'))
        if user and not user.is_admin:
            return f(*args, **kwargs)
        else:
            flash('You do not have permission to access this page')
            return redirect(url_for('admin.admin_dashboard'))
    return inner