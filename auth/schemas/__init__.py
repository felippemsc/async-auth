from marshmallow import Schema, fields


class QueryStringSchema(Schema):
    limit = fields.Integer()
    offset = fields.Integer()
