from marshmallow import Schema, fields

from auth.models.users import User


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    key = fields.String(dump_only=True)
    email = fields.Email()
    created_at = fields.String(dump_only=True)
    updated_at = fields.String(dump_only=True)

    @classmethod
    async def new_key(cls, user_data: dict):
        user_data['key'] = await User.get_new_key()

        return user_data
