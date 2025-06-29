from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from routes.decorators import login_required,admin_required

from models import ParkingLot,ParkingSpot
from config import db
spot_bp = Blueprint('spot', __name__)

