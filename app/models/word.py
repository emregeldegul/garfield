from json import loads

from app import db


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False, unique=True)
    definitions = db.Column(db.JSON, nullable=False)