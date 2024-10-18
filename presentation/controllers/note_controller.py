from flask_smorest import Blueprint
from injector import inject
from domain.schemas import NoteSchema, NoteIDSchema, PaginationResponseSchema, PaginationSchema
from flask import jsonify
from application.services.note_services import NoteService

notes_blp = Blueprint("notes", "notes", url_prefix="/notes")

@notes_blp.route("/")
@notes_blp.arguments(PaginationSchema, location="query")
@notes_blp.response(200, PaginationResponseSchema)
@inject
def get_notes(args, note_service: NoteService):
    pagination_data = note_service.get_all_notes(args.get('page'), args.get('limit'), args.get('search_query'))
    return pagination_data

@notes_blp.route("/<uuid:id>")
@inject
def get_note(id, note_service: NoteService):
    note = note_service.get_note_by_id(id)
    return jsonify({
        'id': note.id,
        'title': note.title,
        'description': note.description,
        'created_at': note.created_at,
        'updated_at': note.updated_at,
    })

@notes_blp.route("/", methods=["POST"])
@notes_blp.arguments(NoteSchema)
@inject
def create_note(data, note_service: NoteService):
    new_note = note_service.create_note(data)
    return jsonify({'message': 'Note created successfully!', 'note': {'id': new_note.id}}), 201

@notes_blp.route("/<uuid:id>", methods=["PUT"])
@notes_blp.arguments(NoteSchema)
@inject
def update_note(data, id, note_service: NoteService):
    note_service.update_note(id, data)
    return jsonify({'message': 'Note updated successfully!'})

@notes_blp.route("/<uuid:id>", methods=["DELETE"])
def delete_note(id, note_service: NoteService):
    note_service.delete_note(id)
    return jsonify({'message': 'Note deleted successfully!'})
