from config import db

class ParkingSpot(db.Model):
    __tablename__ = 'parking_spots'
    id=db.Column(db.Integer, primary_key=True)
    lot_id=db.Column(db.Integer, db.ForeignKey('parking_lots.id'), nullable=False)
    spot_number=db.Column(db.String(50), nullable=False)
    is_ev_spot=db.Column(db.Boolean, default=False)
    status=db.Column(db.String(50), default='available')  
    
    # __table_args__=(db.UniqueConstraint('lot_id', 'spot_number', name='unique_spot_per_lot'))
    
    def __repr__(self):
        return f'<ParkingSpot {self.spot_number} in Lot {self.lot_id}>'