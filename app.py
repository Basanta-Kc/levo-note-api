import os
from dotenv import load_dotenv
from flask import Flask
from flask_injector import FlaskInjector
from flask_smorest import Api
from dependencies import configure
from infrastructure.database import db
from flask_migrate import Migrate
from mail import mail
from presentation import notes_blp, reminders_blp, register_error_handlers
from flask_cors import CORS
import logging
from logging.handlers import RotatingFileHandler
from scheduler_config import initialize_scheduler

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, template_folder="presentation/templates")
app.config.from_object("config.Config")

# Custom filter to get environment variables
@app.template_filter('getenv')
def getenv_filter(key, default_value=None):
    return os.getenv(key, default_value)

# Enable CORS for the entire app
CORS(app, origins="*")

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db, directory="infrastructure/migrations")

# Set up logging
handler = RotatingFileHandler("error.log", maxBytes=100000, backupCount=1)
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)

# Set up email
mail.init_app(app)

# Register blueprints and error handlers
api = Api(app)

api.register_blueprint(notes_blp)
api.register_blueprint(reminders_blp)
register_error_handlers(app)


# Dependency injection configuration
FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
    initialize_scheduler()
    app.run(port=8000)
