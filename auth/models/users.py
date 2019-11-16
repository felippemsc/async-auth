import orm

from auth.models import METADATA, DATABASE


class UserModel(orm.Model):
    __tablename__ = "user"
    __metadata__ = METADATA
    __database__ = DATABASE

    id = orm.Integer(primary_key=True)
    email = orm.String(max_length=100)
