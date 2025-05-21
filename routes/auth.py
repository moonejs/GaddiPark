from flask import Blueprint,render_template

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/login')
def login():
    return render_template('index.html')

@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')