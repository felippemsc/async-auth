import json

from asyncio import CancelledError
from aiohttp import web


async def handle_400(request, ex):
    return web.json_response({"msg": ex.text}, status=400)


async def handle_401(request, ex):
    return web.json_response({"msg": "Unauthorized"}, status=401)


async def handle_404(request, ex):
    return web.json_response({"msg": ex.text}, status=404)


async def handle_422(request, ex):
    return web.json_response({"errors": json.loads(ex.text)}, status=422)


async def handle_499(request, ex):
    return web.json_response({"msg": "Client Closed Request"}, status=499)


async def handle_exceptions(ex):
    return web.json_response(
        {"msg": "{}: {}".format(type(ex).__name__, ex)}, status=500
    )


def create_error_middleware(status_overrides, exception_overrides):
    @web.middleware
    async def error_middleware(request, handler):
        try:
            response = await handler(request)

            override = status_overrides.get(response.status)
            if override:
                return await override(request)
            return response

        except web.HTTPException as ex:
            override = status_overrides.get(ex.status)

            if override:
                return await override(request, ex)
            raise

        except CancelledError as ex:
            override = status_overrides.get(499)

            if override:
                return await override(request, ex)
            raise

        except Exception as ex:
            override = exception_overrides.get(500)

            if override:
                return await override(ex)
            raise

    return error_middleware


ERROR_MIDDLEWARE = create_error_middleware(
    {
        400: handle_400,
        401: handle_401,
        404: handle_404,
        422: handle_422,
        499: handle_499,
    },
    {500: handle_exceptions},
)
