from marshmallow import Schema, fields

from auth.models.users import User
from auth.utils import gen_key


class UserSchema(Schema):
    id = fields.Integer()
    key = fields.String(read_only=True)
    email = fields.Email()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @classmethod
    async def create(cls, data: dict):
        user_dict = cls().load(data)
        user_dict['key'] = await cls.get_new_key()

        return user_dict

    @staticmethod
    async def get_new_key():
        key = gen_key()
        while len(await User.objects.filter(key=key).all()) > 0:
            key = gen_key(9)

        return key
