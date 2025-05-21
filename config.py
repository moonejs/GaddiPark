from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False