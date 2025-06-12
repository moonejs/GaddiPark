from config import db
class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lot_id = db.Column(db.Integer, db.ForeignKey('parking_lots.id'), nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
    
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=True)
    
    def __repr__(self):
        return f'<Rating {self.id} for Booking {self.booking_id}>'