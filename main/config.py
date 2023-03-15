import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

ACCESS_EXPIRES = timedelta(minutes=30)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '4y87jj23rhjkkjbj')
    DEBUG = False
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL', 'postgresql://postgres:docker@localhost:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fheskfh676478324jfdh')


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
