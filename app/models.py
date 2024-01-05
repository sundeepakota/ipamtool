# Example models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class IPAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subnet = db.Column(db.String(20), unique=True, nullable=False)
    location = db.Column(db.String(100))
    comments = db.Column(db.Text)
    # Add other fields as needed
