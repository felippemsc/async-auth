from aiohttp import web

from auth.database import init_pg
# from .middleware import ERROR_MIDDLEWARE

from auth.views import Index
from auth.views.users import UserView


def create_app():
    """
    Fábrica da aplicação

    :return: Um objeto de aplicação
    """
    app = web.Application()

    app.on_startup.append(init_pg)

    app.router.add_view('/', Index)
    app.router.add_view('/user', UserView)

    # app.middlewares.append(ERROR_MIDDLEWARE)

    return app
