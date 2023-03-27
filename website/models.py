from . import db
from sqlalchemy import func

class Besked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    besked = db.Column(db.String(10000))