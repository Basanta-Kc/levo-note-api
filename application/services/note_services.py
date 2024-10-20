from injector import inject
from infrastructure import NoteRepository
from infrastructure import ReminderRepository


class NoteService:
    @inject
    def __init__(
        self, note_repository: NoteRepository, reminder_repository: ReminderRepository
    ):
        self.note_repository = note_repository
        self.reminder_repository = reminder_repository

    def get_all_notes(self, page, limit, search_query):
        return self.note_repository.get_all_notes(page, limit, search_query)

    def get_note_by_id(self, note_id):
        return self.note_repository.get_note_by_id(note_id)

    def create_note(self, data):
        return self.note_repository.create_note(data)

    def update_note(self, note_id, data):
        note = self.note_repository.get_note_by_id(note_id)
        return self.note_repository.update_note(note, data)

    def delete_note(self, note_id):
        note = self.note_repository.get_note_by_id(note_id)
        self.note_repository.delete_note(note)
        if note.reminder:
            self.reminder_repository.delete_reminder(note.reminder)
