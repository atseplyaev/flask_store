import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'store.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    FLASK_ADMIN_SWATCH = 'cerulean'


class DevelopConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
