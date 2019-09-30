import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'mma'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    APP_HOST = 'http://'
    DM_FILENAME = 'DM.yml'
    # celery
    CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
    CELERY_RESULT_PERSISTENT = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    APP_HOST = 'http://localhost:4200'


class TestingConfig(Config):
    TESTING = True
