from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # One-to-Many relationship: A user can have multiple CVs
    cvs = db.relationship('CV', backref='user', lazy=True)


class CV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_title = db.Column(db.String(100))
    summary = db.Column(db.Text)

    # Relationships to other tables
    personal_details = db.relationship('PersonalDetails', backref='cv', uselist=False)
    employments = db.relationship('Employment', backref='cv', lazy=True)
    education = db.relationship('Education', backref='cv', lazy=True)
    languages = db.relationship('Languages', backref='cv', lazy=True)
    websites = db.relationship('Websites', backref='cv', lazy=True)


class PersonalDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50))
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))


class Employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    location = db.Column(db.String(150))


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    degree = db.Column(db.String(150), nullable=False)
    institution = db.Column(db.String(150))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)


class Languages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50))


class Websites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    label = db.Column(db.String(100))
    url = db.Column(db.String(255))
