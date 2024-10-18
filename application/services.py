from injector import inject
from infrastructure.repositories import NoteRepository


class NoteService:
    @inject
    def __init__(self, note_repository: NoteRepository):
        self.note_repository = note_repository

    def get_all_notes(self, page, limit, search_query):
        return self.note_repository.get_all_notes(page, limit, search_query)

    def get_note_by_id(self, note_id):
        return self.note_repository.get_note_by_id(note_id)

    def create_note(self, data):
        print(data)
        return self.note_repository.create_note(data)

    def update_note(self, note_id, data):
        note = self.note_repository.get_note_by_id(note_id)
        return self.note_repository.update_note(note, data)

    def delete_note(self, note_id):
        note = self.note_repository.get_note_by_id(note_id)
        self.note_repository.delete_note(note)
