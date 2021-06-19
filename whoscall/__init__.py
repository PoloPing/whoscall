import os
from whoscall.utils.load import load_settings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(name=None):
    settings = load_settings(os.getenv('FLASK_SETTINGS', 'whoscall.settings.base'))
    name = __name__ if not name else name
    app = Flask(name)

    DATABASE_NAME = settings['DATABASES']['default']['NAME']
    DATABASE_USER = settings['DATABASES']['default']['USER']
    DATABASE_PASSWORD = settings['DATABASES']['default']['PASSWORD']
    DATABASE_SERVICE = settings['DATABASES']['default']['HOST']
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVICE}/{DATABASE_NAME}'

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    return app
