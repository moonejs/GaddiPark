from config import db
class favLocation(db.Model):
    __tablename__ = 'fav_locations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lot_id = db.Column(db.Integer, db.ForeignKey('parking_lots.id'), nullable=False)
    def __repr__(self):
        return f'<FavLocation {self.location_name} for User {self.user_id}>'