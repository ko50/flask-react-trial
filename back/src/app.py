from flask import Flask

from back.main import CONFIG
from .database import init_db


def create_app() -> Flask:
    app = Flask(__name__,
                static_folder='../front/build/static',
                template_folder='../front/build')

    app.config.from_object(CONFIG)

    init_db(app)

    return app
