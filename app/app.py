import logging
from flask import Flask
import domain as d
import interfaces.handlers as h
from infraestructure.config import Config

APP = Flask(__name__)

CONFIG: Config = Config()

# Logger initial conf
LOGGER = logging.getLogger(CONFIG.logger.LogLevel)
LOGGER.handlers.extend(LOGGER.handlers)
LOGGER.setLevel(LOGGER.level)
LOGGER.info(CONFIG)


@APP.route("/healthcheck", methods=['GET'])
def healthCheck() -> d.JSONType:
    '''healthCheck route'''
    return h.healthCheckHandler()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    APP.run(*CONFIG.server, threaded=True)
