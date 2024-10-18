from flask import Flask
from flask_injector import FlaskInjector
from flask_smorest import Api
from dependencies import configure
from infrastructure.database import db
from flask_migrate import Migrate
from presentation.controllers import notes_blp
from presentation.error_handlers import register_error_handlers

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db, directory='infrastructure/migrations') 

# Set up logging
handler = RotatingFileHandler('error.log', maxBytes=100000, backupCount=1)
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)

# Register blueprints and error handlers
api = Api(app)
api.register_blueprint(notes_blp)
register_error_handlers(app)

# Dependency injection configuration
FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(debug=True, port=3000)
