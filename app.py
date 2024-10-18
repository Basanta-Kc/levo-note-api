from flask import Flask, request, jsonify
from flask_smorest import Api, Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate
from marshmallow.exceptions import ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5435/notedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

# Model for the Note table
class Note(db.Model):
    id = db.Column(db.UUID(as_uuid=True) , primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Route to get all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([{'id': note.id, 'title': note.title, 'description': note.description, 
                     'created_at': note.created_at, 'updated_at': note.updated_at} for note in notes])

# Route to get a single note by ID
@app.route('/notes/<id>', methods=['GET'])
def get_note(id):
    note = Note.query.get_or_404(id)
    return jsonify({'id': note.id, 'title': note.title, 'description': note.description,
                    'created_at': note.created_at, 'updated_at': note.updated_at})

# Route to create a new note
@app.route('/notes', methods=['POST'])
def create_note():
    data = request.json
    new_note = Note(title=data['title'], description=data['description'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify({'message': 'Note created successfully!', 'note': {'id': new_note.id}}), 201

# Route to update a note
@app.route('/notes/<id>', methods=['PUT'])
def update_note(id):
    note = Note.query.get_or_404(id)
    data = request.json
    note.title = data.get('title', note.title)
    note.description = data.get('description', note.description)
    db.session.commit()
    return jsonify({'message': 'Note updated successfully!'})

# Route to delete a note
@app.route('/notes/<id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

