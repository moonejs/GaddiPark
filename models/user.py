from config import db

class User(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password_hash=db.Column(db.String(128),nullable=False)
    full_name=db.Column(db.String(80),nullable=True)
    is_admin=db.Column(db.Boolean,default=False)
    wallet_balance=db.Column(db.Float,default=0.00)
    def __repr__(self):
        return f'<User {self.username}>'