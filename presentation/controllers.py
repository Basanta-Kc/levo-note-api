from flask_smorest import Blueprint
from injector import inject
from domain.schemas import NoteSchema, NoteIDSchema, PaginationSchema
from flask import jsonify, current_app, request
from application.services import NoteService

notes_blp = Blueprint("notes", "notes", url_prefix="/notes")

@notes_blp.route("/")
@notes_blp.arguments(PaginationSchema, location="query")
@inject
def get_notes(args, note_service: NoteService):
    current_app.logger.debug(f"Received arguments: {args}")  # Use current_app to log messages
    pagination_data = note_service.get_all_notes(args.get('page'), args.get('limit'), args.get('search_query'))
    return jsonify({
            'total': pagination_data['total'],
            'items': [{
                'id': note.id,
                'title': note.title,
                'description': note.description,
                'created_at': note.created_at,
                'updated_at': note.updated_at
            } for note in pagination_data['items']]
        })

@notes_blp.route("/<uuid:id>")
@notes_blp.arguments(NoteIDSchema, location="view_args")
@inject
def get_note(args, note_service: NoteService):
    note = note_service.get_note_by_id(args['id'])
    return jsonify({
        'id': note.id,
        'title': note.title,
        'description': note.description,
        'created_at': note.created_at,
        'updated_at': note.updated_at
    })

@notes_blp.route("/", methods=["POST"])
@notes_blp.arguments(NoteSchema)
@inject
def create_note(data, note_service: NoteService):
    new_note = note_service.create_note(data)
    return jsonify({'message': 'Note created successfully!', 'note': {'id': new_note.id}}), 201

@notes_blp.route("/<uuid:id>", methods=["PUT"])
@notes_blp.arguments(NoteIDSchema, location="view_args")
@notes_blp.arguments(NoteSchema)
@inject
def update_note(args, data, note_service: NoteService):
    updated_note = note_service.update_note(args['id'], data)
    return jsonify({'message': 'Note updated successfully!'})

@notes_blp.route("/<uuid:id>", methods=["DELETE"])
@notes_blp.arguments(NoteIDSchema, location="view_args")
def delete_note(args, note_service: NoteService):
    note_service.delete_note(args['id'])
    return jsonify({'message': 'Note deleted successfully!'})
