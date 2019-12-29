# -*- coding: utf-8 -*-
import pytest

from auth import create_app


@pytest.fixture
def client(loop, aiohttp_client):
    app = create_app()
    return loop.run_until_complete(aiohttp_client(app))
