from flask_sqlalchemy import SQLAlchemy
import os 

db=SQLAlchemy()
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False