# -*- coding: utf-8 -*-
import pytest

from auth import create_app
from auth.database import drop_pg


@pytest.fixture
def client(loop, aiohttp_client):
    app = create_app()
    loop.run_until_complete(drop_pg())
    return loop.run_until_complete(aiohttp_client(app))
