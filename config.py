import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost:5435/notedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_TITLE = "My API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')
    DEBUG = True


class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://postgres:password@localhost:5435/test_notedb')


class ProductionConfig(Config):
    """Production configuration class."""
    DEBUG = False
