from injector import singleton
from application.services import NoteService
from infrastructure.repositories import NoteRepository

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