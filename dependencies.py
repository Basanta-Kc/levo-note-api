from injector import singleton
from application.services.note_services import NoteService
from infrastructure.repositories.note_repository import NoteRepository

def configure(binder):
    binder.bind(
        NoteRepository,
        to=NoteRepository,
        scope=singleton
    )
    binder.bind(
        NoteService,
        to=NoteService,
        scope=singleton
    )