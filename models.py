# models.py
import flask_sqlalchemy
from app import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    message = db.Column(db.String(255))
    def __init__(self, a, b):
        self.name = a
        self.message = b
        
    def __repr__(self):
        return '<Chat message: %s>' % self.message
