from datetime import datetime

import orm

from asyncpg.exceptions import UniqueViolationError

from auth.models import METADATA, DATABASE, ModelExceptions
from auth.utils import gen_key


class EmailAlreadyExists(ModelExceptions):
    pass


class User(orm.Model):
    __tablename__ = "user"
    __metadata__ = METADATA
    __database__ = DATABASE

    id = orm.Integer(primary_key=True)
    key = orm.String(max_length=8, unique=True, index=True)
    email = orm.String(max_length=100, unique=True)
    created_at = orm.DateTime(default=datetime.now())
    updated_at = orm.DateTime(allow_null=True)

    @classmethod
    async def save(cls, user: dict):
        user['key'] = await cls.get_new_key()
        try:
            return await cls.objects.create(**user)
        except UniqueViolationError:
            raise EmailAlreadyExists('e-mail already exists')

    @classmethod
    async def get_new_key(cls, key_lenth: int = 8):
        key = gen_key(key_lenth)
        while await cls.objects.filter(key=key).exists():
            key = gen_key(key_lenth)

        return key
