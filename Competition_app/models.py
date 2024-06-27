from app import db
from User_app.models import BaseModel

class Competition(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    social_issue = db.Column(db.ARRAY(db.String(255)), nullable=False)  # Assuming PostgreSQL with ARRAY type
    
    # this foreign key is primary key of user table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)

    # reference of Entry table(Entry table use this table's PK as FK)
    entries = db.relationship('Entry', backref='competition', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Competition {self.title}>'
    