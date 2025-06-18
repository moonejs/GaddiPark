from flask import Blueprint,render_template,request,redirect,url_for,session
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from config import db


auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username =request.form.get('username')
        password =request.form.get('password')
        
        if not username or not password:
            return render_template('index.html', error='Username and password are required')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash,password):
            session['user_id']=user.id
            if user.is_admin:
                return redirect(url_for('admin.admin_dashboard'))
            else:
                return "Login successful"
            
        
        return render_template('index.html', error='Invalid username or password')
    else:
        return render_template('index.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username= request.form.get('username')
        password =request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        fullname=request.form.get('fullname')
        
        #checks
        if not username or not password or not confirm_password or not fullname:
            return render_template('signup.html', error='All fields are required')
        
        if password != confirm_password:
            return render_template('signup.html', error='Passwords do not match')
        
        user=User.query.filter_by(username=username).first()
        
        if user:
            return render_template('signup.html', error='Username already exists')
        
        password_hash = generate_password_hash(password)
        
        
        new_user = User(username=username,password_hash=password_hash,full_name=fullname)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html')
    