from domain.models import Note, db

class NoteRepository:
    def get_all_notes(self, page, limit, search_query=None):
        query = Note.query
        
        # Apply search filter if provided
        if search_query:
            query = query.filter(
                Note.title.ilike(f'%{search_query}%') | Note.description.ilike(f'%{search_query}%')
            )

        # Paginate the results
        pagination = query.paginate(page=page, per_page=limit)
        
        return {
            'total': pagination.total,
            'items': pagination.items
        }

    def get_note_by_id(self, note_id):
        return Note.query.get_or_404(note_id)

    def create_note(self, data):
        new_note = Note(**data)
        db.session.add(new_note)
        db.session.commit()
        return new_note

    def update_note(self, note, data):
        note.title = data.get('title', note.title)
        note.description = data.get('description', note.description)
        db.session.commit()
        return note

    def delete_note(self, note):
        db.session.delete(note)
        db.session.commit()
