from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if 'user_id'  in session:
            return f(*args, **kwargs)
        else:
            flash('Please login to continue')
            return redirect(url_for('auth.login'))
    return inner