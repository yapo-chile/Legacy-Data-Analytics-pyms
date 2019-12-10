import domain as d
from .handler import Response
import os

def healthCheckHandler() -> d.JSONType:
    r = Response(200)
    return r.toJson(msg=d.JSONType({"status": "OK"}))
