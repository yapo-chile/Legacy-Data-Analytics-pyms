import domain as d
from .logger import Response

def healthCheckHandler() -> d.JSONType:
    return Response(d.HTTPStatus(200)).Success('OK')
