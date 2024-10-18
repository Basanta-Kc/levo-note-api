from flask import Flask, request, jsonify
from flask_smorest import Api, Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import ValidationError
from datetime import datetime, timezone
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5435/notedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

# Blueprint for Notes API
notes_blp = Blueprint("notes", "notes", url_prefix="/notes")

# Note model
class Note(db.Model):
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

# Register the validation schemas
from marshmallow import Schema, fields, validate

# Schema for request body validation
class NoteSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=True, validate=validate.Length(min=1))

# Schema for query parameter validation
class PaginationSchema(Schema):
    page = fields.Integer(missing=1, validate=validate.Range(min=1))
    limit = fields.Integer(missing=10, validate=validate.Range(min=1, max=100))

# Schema for URL parameter validation
class NoteIDSchema(Schema):
    id = fields.UUID(required=True)

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

# Route to get all notes with query parameters validation
@notes_blp.route("/")
@notes_blp.arguments(PaginationSchema, location="query")
def get_notes(args):
    """Retrieve all notes with pagination."""
    page = args.get('page')
    limit = args.get('limit')
    notes = Note.query.paginate(page=page, per_page=limit).items
    return jsonify([{'id': note.id, 'title': note.title, 'description': note.description,
                     'created_at': note.created_at, 'updated_at': note.updated_at} for note in notes])

# Route to get a single note by ID with URL parameter validation
@notes_blp.route("/<uuid:id>")
@notes_blp.arguments(NoteIDSchema, location="view_args")
def get_note(args):
    """Retrieve a single note by its ID."""
    note = Note.query.get_or_404(args['id'])
    return jsonify({'id': note.id, 'title': note.title, 'description': note.description,
                    'created_at': note.created_at, 'updated_at': note.updated_at})

# Route to create a new note with body validation
@notes_blp.route("/", methods=["POST"])
@notes_blp.arguments(NoteSchema)
def create_note(data):
    """Create a new note."""
    new_note = Note(**data)
    db.session.add(new_note)
    db.session.commit()
    return jsonify({'message': 'Note created successfully!', 'note': {'id': new_note.id}}), 201

# Route to update a note by ID with validation
@notes_blp.route("/<uuid:id>", methods=["PUT"])
@notes_blp.arguments(NoteIDSchema, location="view_args")
@notes_blp.arguments(NoteSchema)
def update_note(args, data):
    """Update an existing note by ID."""
    note = Note.query.get_or_404(args['id'])
    note.title = data.get('title', note.title)
    note.description = data.get('description', note.description)
    db.session.commit()
    return jsonify({'message': 'Note updated successfully!'})

# Route to delete a note by ID with validation
@notes_blp.route("/<uuid:id>", methods=["DELETE"])
@notes_blp.arguments(NoteIDSchema, location="view_args")
def delete_note(args):
    """Delete a note by its ID."""
    note = Note.query.get_or_404(args['id'])
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note deleted successfully!'})

api.register_blueprint(notes_blp)

if __name__ == '__main__':
    app.run(debug=True)
