from marshmallow import Schema, fields, validate, post_load


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    key = fields.String(dump_only=True)
    email = fields.Email()
    password = fields.String(load_only=True, validate=validate.Length(min=8, max=20))
    created_at = fields.String(dump_only=True)
    updated_at = fields.String(dump_only=True)
