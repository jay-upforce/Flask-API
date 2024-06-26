from datetime import datetime
from Competition_app import db
from User_app.models import BaseModel

class Competition(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    social_issue = db.Column(db.ARRAY(db.String(255)), nullable=False)  # Assuming PostgreSQL with ARRAY type
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)