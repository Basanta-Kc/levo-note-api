from injector import singleton
from application.services.note_services import NoteService
from infrastructure import NoteRepository


def configure(binder):
    binder.bind(NoteRepository, to=NoteRepository, scope=singleton)
    binder.bind(NoteService, to=NoteService, scope=singleton)
