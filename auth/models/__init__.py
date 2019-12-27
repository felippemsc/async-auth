import databases
import sqlalchemy

from dynaconf import settings

DATABASE_URI = (
    f"postgresql://{settings.DB.user}:{settings.DB.password}@"
    f"{settings.DB.host}:{settings.DB.port}/{settings.DB.name}"
)
DATABASE = databases.Database(DATABASE_URI)
METADATA = sqlalchemy.MetaData(schema=settings.DB.schema)


class ModelExceptions(Exception):
    def __init__(self, msg):
        self.msg = msg
