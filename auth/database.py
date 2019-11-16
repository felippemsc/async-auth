import sqlalchemy

from dynaconf import settings
from auth.models import METADATA, DATABASE


async def init_pg(app):
    engine = sqlalchemy.create_engine(str(DATABASE.url))
    engine.connect().execute(f'CREATE SCHEMA IF NOT EXISTS {settings.DB.schema}')
    METADATA.create_all(engine)
    await DATABASE.connect()
