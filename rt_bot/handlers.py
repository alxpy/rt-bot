from rt_bot.utils import jsonify


@jsonify
async def event(request):
    return {'hello': 'world'}, 200


def set_routes(app):
    app.router.add_get('/event', event)
