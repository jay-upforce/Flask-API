from app import db
from User_app.models import BaseModel

class Entry(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    how_did_you_hear = db.Column(db.String(255), nullable=False)
    is_entrant_part_of_institution = db.Column(db.Boolean, default=False)
    i_am_part_of = db.Column(db.String(200), nullable=True) 
    
    # this foreign key is primary key of competition table
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f'<Entry {self.name} ({self.country})>'
