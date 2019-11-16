from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    key = fields.String(dump_only=True)
    email = fields.Email()
    created_at = fields.String(dump_only=True)
    updated_at = fields.String(dump_only=True)
