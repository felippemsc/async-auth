import databases
import sqlalchemy

from dynaconf import settings

DATABASE = databases.Database(
    f'postgresql://{settings.DB.user}:{settings.DB.password}@{settings.DB.host}:{settings.DB.port}/{settings.DB.name}'
)
METADATA = sqlalchemy.MetaData(schema=settings.DB.schema)
