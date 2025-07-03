from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from routes.decorators import login_required


from config import db


auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/login' , methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username =request.form.get('username')
        password =request.form.get('password')
        
        if not username or not password:
            flash('Username and password are required')
            return render_template('login.html')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash,password):
            session['user_id']=user.id
            if user.is_admin:
                flash('Login Successfully!','success')
                return redirect(url_for('admin.admin_dashboard'))
            else:
                flash('Login Successfully!','success')
                return redirect(url_for('user.user_dashboard'))
            
        flash('Invalid username or password',"error")
        return redirect(url_for('auth.login'))
    else:
        return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username= request.form.get('username')
        password =request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        fullname=request.form.get('fullname')
        
        
        if not username or not password or not confirm_password or not fullname:
            flash('All fields are required',"error")
            return redirect(url_for('auth.signup'))
        
        if password != confirm_password:
            flash('Passwords do not match',"error")
            return redirect(url_for('auth.signup'))
        
        user=User.query.filter_by(username=username).first()
        
        if user:
            flash('Username already exists',"error")
            return redirect(url_for('auth.signup'))
        
        password_hash = generate_password_hash(password)
        
        
        new_user = User(username=username,password_hash=password_hash,full_name=fullname)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!',"success")
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html')
    

@auth_bp.route('/logout')
@login_required
def logout():
    session.pop('user_id')
    flash('You have been logged out',"success")
    return redirect(url_for('auth.login'))