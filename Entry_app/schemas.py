from marshmallow import Schema, fields, validate

class EntrySerializer(Schema):
    id = fields.Int(dump_only=True)     # primary key
    name = fields.Str(required=True, validate=validate.Length(min=1))
    country = fields.Str(required=True, validate=validate.Length(min=2))
    state = fields.Str(required=True, validate=validate.Length(min=2))
    how_did_you_hear = fields.Str(required=True, validate=validate.Length(min=1))
    is_entrant_part_of_institution = fields.Bool(required=True)
    i_am_part_of = fields.Str()
    competition_id = fields.Int(required=True)     # foreign key
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_delete = fields.Bool(dump_only=True)
    is_active = fields.Bool(dump_only=True)
