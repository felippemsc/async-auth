import databases
import sqlalchemy

from dynaconf import settings

DATABASE = databases.Database(
    f"postgresql://{settings.DB.user}:{settings.DB.password}@{settings.DB.host}:{settings.DB.port}/{settings.DB.name}"
)
METADATA = sqlalchemy.MetaData(schema=settings.DB.schema)


class ModelExceptions(Exception):
    def __init__(self, msg):
        self.msg = msg
