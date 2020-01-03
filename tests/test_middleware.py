from aiohttp import web

from auth.middleware import ERROR_MIDDLEWARE


class UnexpectedError(web.HTTPClientError):
    status_code = 444


class TestMiddleware:
    async def test_health_check(self, loop, aiohttp_client):
        async def handler(request):
            raise UnexpectedError

        app = web.Application()
        app.middlewares.append(ERROR_MIDDLEWARE)
        app.router.add_route('GET', '/', handler)

        client = await aiohttp_client(app)
        resp = await client.get('/')

        assert resp.status == 444
