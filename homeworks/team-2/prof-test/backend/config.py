import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'my-key-is-very-secret-becouse-he-have-siiiskiii'
    SQLALCHEMY_DATABASE_URI = "postgresql://dima:12124343@localhost/proftest"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
