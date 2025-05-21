from config import db

class ParkingLot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)
    total_spots = db.Column(db.Integer, nullable=False)
    occupied_spots = db.Column(db.Integer, default=0)
    ev_spots = db.Column(db.Integer, default=0)
    ev_charging_rate = db.Column(db.Float, nullable=True)
    opening_time = db.Column(db.String(10), nullable=False)
    closing_time = db.Column(db.String(10), nullable=False)
    is_24_hours = db.Column(db.Boolean, default=False)
    discription = db.Column(db.String(200), nullable=True)
    def __repr__(self):
        return f'<ParkingLot {self.name}>'