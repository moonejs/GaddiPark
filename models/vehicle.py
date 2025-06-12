from config import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50),nullable=False)
    registration_number = db.Column(db.String(20),nullable=False,unique=True)
    is_ev= db.Column(db.Boolean,default=False)
    
    def __repr__(self):
        return f'<Vehicle {self.registration_number}>'