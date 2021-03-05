from flask import Flask

from .src.config import Config, DevelopmentConfig
from .src.app import create_app


CONFIG: Config = DevelopmentConfig()
APP: Flask = create_app()

if __name__ == "__main__":
    APP.run(debug=True)
