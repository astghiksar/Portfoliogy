import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Astghiksar1@localhost:5432/portfoliogy_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # Used for session management
