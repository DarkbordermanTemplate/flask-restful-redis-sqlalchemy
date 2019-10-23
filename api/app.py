import os

from flask import Flask
from flask_restful import Api
from werkzeug.exceptions import HTTPException, default_exceptions
from dotenv import load_dotenv

from endpoints import RESOURCES
from config import APP_CONFIG
from db import sql, redis

load_dotenv()


def create_app(config_mode):

    app = Flask(__name__)

    @app.errorhandler(Exception)
    def handle_error(error):

        code = 500

        if isinstance(error, HTTPException):
            code = error.code

        return {'error': str(error)}, code

    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)

    # flask config
    app.config.from_object(APP_CONFIG[config_mode])

    # DB Init
    sql.init_app(app)
    redis.init_app(app)
    # Route Init
    api = Api(app)
    for route in RESOURCES:
        api.add_resource(RESOURCES[route], route)

    # pylint: enable=W0612

    return app


def main():
    config_name = os.environ.get('APP_SETTINGS', 'development')
    app = create_app(config_name)
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
