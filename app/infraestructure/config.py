import json
from os import environ
from typing import NamedTuple


# Logger tuple that contain all definitions for logging usage
class Logger(NamedTuple):
    LogLevel: str = environ.get("LOGGER_LOG_LEVEL", "gunicorn.error")


# Server tuple that contains all definitions for server init
class Server(NamedTuple):
    Host: str = environ.get("SERVER_HOST", "0.0.0.0")
    Port: int = int(environ.get("SERVER_PORT", 5000))
    Debug: bool = json.loads(environ.get("SERVER_DEBUG", 'true'))


# Database tuple that contains all definitions for its conection
class Database(NamedTuple):
    Host: str = environ.get("DATABASE_HOST", "0.0.0.0")
    Port: int = int(environ.get("DATABASE_PORT", 5432))
    Name: str = environ.get("DATABASE_NAME", "feeds-db")
    User: str = environ.get("DATABASE_USER", "docker")
    Password: str = environ.get("DATABASE_PASSWORD", "")


# Config type to contain all definitions of configs
class Config(NamedTuple):
    logger: Logger = Logger()
    server: Server = Server()
    database: Database = Database()
