from . import db
from flask_login import UserMixin
from datetime import datetime


class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    note = db.Column(db.String(200))
    amount = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class WaterIntake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cup = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Weight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Double)
    date = db.Column(db.DateTime(timezone=True),nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    trainings = db.relationship('Training')
    cups = db.relationship('WaterIntake')
    weight = db.relationship('Weight')
