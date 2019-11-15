from aiohttp import web

# from .database import init_pg, close_pg
# from .middleware import ERROR_MIDDLEWARE

from auth.views import Index


def create_app(config):
    """
    Fábrica da aplicação

    :param config: um objeto de configuração. Pode ser um objeto Python
    ou uma string representando o módulo
    :return: Um objeto de aplicação
    """
    app = web.Application()

    app['config'] = config

    # app.on_startup.append(init_pg)
    # app.on_cleanup.append(close_pg)

    app.router.add_view('/', Index)

    # app.middlewares.append(ERROR_MIDDLEWARE)

    return app
