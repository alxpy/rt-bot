import json
from functools import wraps

from aiohttp import web


def json_response(data, status):
    content_type = 'application/json'
    return web.Response(
        text=json.dumps(data),
        content_type=content_type,
        status=status,
    )


def jsonify(handler):
    @wraps(handler)
    async def wrap(request):
        return json_response(*await handler(request))
    return wrap
