from marshmallow import Schema, fields, validate,validates, ValidationError
from .models import User

class UserSerializer(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1), error_messages={"required": "Name is required."})
    email = fields.Email(required=True, error_messages={"required": "Email is required."})
    gender = fields.Str(required=True, validate=validate.OneOf(["M", "F"]), error_messages={"required": "Gender is required."})
    phone_number = fields.Str(required=True, validate=validate.Length(min=10, max=15), error_messages={"required": "Phone number is required."})
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_delete = fields.Bool(dump_only=True)
    is_active = fields.Bool(dump_only=True)

    @validates('email')
    def validate_email(self, value):
        # Check if email is already present in the database
        existing_user = User.query.filter_by(email=value).first()
        if existing_user:
            raise ValidationError('Email address already exists')

        # Check if email is a valid format
        if '@' not in value or '.' not in value:
            raise ValidationError('Invalid email address')