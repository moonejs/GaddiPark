from config import db   
from datetime import datetime


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer , primary_key=True)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id') ,nullable=False)
    vehicle_id = db.Column(db.Integer ,db.ForeignKey('vehicles.id') , nullable=False )
    lot_id = db.Column(db.Integer , db.ForeignKey('parking_lots.id') , nullable=False)
    spot_id = db.Column(db.Integer , db.ForeignKey('parking_spots.id') , nullable=False)
    booking_time = db.Column(db.DateTime , default=datetime.utcnow)
    start_time = db.Column(db.DateTime , nullable=False)
    end_time = db.Column(db.DateTime , nullable=True)
    status = db.Column(db.String , nullable=False , default='confirmed')
    amount = db.Column(db.Float , default=0.0)