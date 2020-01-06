# -*- coding: utf-8 -*-
import pytest

from asyncio import CancelledError

from aiohttp import web

from auth import create_app
from auth.database import drop_pg
from auth.middleware import ERROR_MIDDLEWARE
from auth.models.users import User

from tests import fake


class UnexpectedError(web.HTTPClientError):
    status_code = 444


class BroadException(Exception):
    pass


@pytest.fixture
def client(loop, aiohttp_client):
    app = create_app()
    yield loop.run_until_complete(aiohttp_client(app))
    loop.run_until_complete(drop_pg())


@pytest.fixture
def mid_client(loop, aiohttp_client):
    async def unexpected_handler(request):
        raise UnexpectedError

    async def handler_401(request):
        raise web.HTTPUnauthorized

    async def handler_404(request):
        raise web.HTTPNotFound(text='Testing Not Found')

    async def handler_499(request):
        raise CancelledError

    async def handler_500(request):
        raise BroadException('Hello, I`m an Exception')

    app = web.Application()
    app.middlewares.append(ERROR_MIDDLEWARE)
    app.router.add_route('GET', '/unexpected', unexpected_handler)
    app.router.add_route('GET', '/unauthorized', handler_401)
    app.router.add_route('GET', '/not-found', handler_404)
    app.router.add_route('GET', '/client-closed', handler_499)
    app.router.add_route('GET', '/exception', handler_500)

    return loop.run_until_complete(aiohttp_client(app))


@pytest.fixture
def create_users(loop):
    users = [
        {"email": fake.email(), "password": fake.password()} for _ in range(10)
    ]

    for user in users:
        loop.run_until_complete(User.save(user))
