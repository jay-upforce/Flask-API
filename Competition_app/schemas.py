from marshmallow import Schema, fields, validate

class CompetitionSerializer(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1))
    social_issue = fields.List(fields.Str(), required=True)
    user_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_delete = fields.Bool(dump_only=True)
    is_active = fields.Bool(dump_only=True)
