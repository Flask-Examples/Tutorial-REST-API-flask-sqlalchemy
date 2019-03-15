"""
Make a REST API with Flask and SQLAlchemy

Tutorial-REST-API-flask-sqlalchemy

Homepage and documentation:


License: GNU GENERAL PUBLIC LICENSE Version 3

tempo: 
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .view import bp_main
from .model import configure as config_db
from .serealizer import configure as config_ma


def create_app():
    """Create app and config blueprint."""

    # App configure
    app = Flask(__name__)

    # Path configure
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Database configure
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init db
    config_db(app)

    # Init ma
    config_ma(app)    

    # Blueprint configure
    app.register_blueprint(bp_main, url_prefix='/api/v1.0/')    

    return app
