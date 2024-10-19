from flask import jsonify
from marshmallow import ValidationError

def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify(error.messages), 400

    @app.errorhandler(Exception)
    def internal_server_error(error):
        print(error)
        app.logger.error('Server Error: %s', error)
        return jsonify({'message': 'Something went wrong. Please try again later.'}), 500
