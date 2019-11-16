from datetime import datetime

import orm

from auth.models import METADATA, DATABASE


class User(orm.Model):
    __tablename__ = "user"
    __metadata__ = METADATA
    __database__ = DATABASE

    id = orm.Integer(primary_key=True)
    key = orm.String(max_length=8, unique=True, index=True)
    email = orm.String(max_length=100, unique=True)
    created_at = orm.DateTime(default=datetime.now())
    updated_at = orm.DateTime(allow_null=True)
