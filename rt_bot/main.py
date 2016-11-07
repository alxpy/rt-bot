from aiohttp import web

from rt_bot.handlers import set_routes


def create_app():
    app = web.Application()
    set_routes(app)
    return app


def main():
    app = create_app()
    web.run_app(app)
