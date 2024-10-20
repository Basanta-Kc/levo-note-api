import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    # API configuration
    API_TITLE = os.getenv('API_TITLE')
    API_VERSION = os.getenv('API_VERSION')
    OPENAPI_VERSION = os.getenv('OPENAPI_VERSION')

    # Logging and Debugging
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL')
    DEBUG = os.getenv('DEBUG').lower() == 'true'
    
    # Email settings
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS').lower() == 'true'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL').lower() == 'true'


