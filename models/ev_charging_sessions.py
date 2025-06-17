from config import db
from datetime import datetime
class EvChargingSession(db.Model):
    __tablename__ = 'ev_charging_sessions'
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
    
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    energy_consumed = db.Column(db.Float, nullable=True)  
    charging_rate = db.Column(db.Float, nullable=True)
    charging_fee = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(50), default='in_progress') 

    def __repr__(self):
        return f'<EVChargingSession for Booking {self.booking_id}>'