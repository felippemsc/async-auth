from marshmallow import Schema, fields

from auth.models.users import User


class UserSchema(Schema):
    id = fields.Integer()
    key = fields.String(read_only=True)
    email = fields.Email()
    # created_at = fields.DateTime()
    # updated_at = fields.DateTime()

    @classmethod
    async def new_key(cls, user_data: dict):
        user_data['key'] = await User.get_new_key()

        return user_data
