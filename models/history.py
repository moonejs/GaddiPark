from config import db
from datetime import datetime

class History(db.Model):
    __tablename__='history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    lot_id = db.Column(db.Integer, db.ForeignKey('parking_lots.id'), nullable=False)
    spot_id = db.Column(db.Integer, db.ForeignKey('parking_spots.id'), nullable=False)
    entry_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    exit_time = db.Column(db.DateTime, nullable=True)
    booking_id = db.Column(db.String(100), nullable=False)
    transaction_id = db.Column(db.String(100), nullable=False)
    total_amount_paid = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Float, nullable=True)  
    payment_method = db.Column(db.String(50), nullable=True)
    is_ev_spot = db.Column(db.Boolean, nullable=False, default=False)