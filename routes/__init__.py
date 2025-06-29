from .auth import auth_bp
from .admin import admin_bp
from .user import user_bp
from .profile import profile_bp
from .parking import parking_bp
from .booking import booking_bp
from .payment import payment_bp
all_blueprints = [auth_bp, admin_bp,user_bp,profile_bp,parking_bp,booking_bp,payment_bp]