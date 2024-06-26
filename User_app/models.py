from User_app import db

class BaseModel(db.Model):
    __abstract__ = True
    # Fix columns
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    is_delete = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)


class User(BaseModel):
    __tablename__ = 'users'  # table name
    
    # New Columns with BaseModel Columns
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    gender = db.Column(db.String(10))
    phone_number = db.Column(db.String(20))

    competitions = db.relationship('Competition', backref='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.name}>"
    