# models.py
"""This is a file that creats the database"""
import flask_sqlalchemy
from app import DB


class Chat(DB.Model):
    """Creat class for the database"""

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(255))
    message = DB.Column(DB.String(255))

    def __init__(self, a, b):
        self.name = a
        self.message = b

    def __repr__(self):
        return "<Chat message: %s>" % self.message
