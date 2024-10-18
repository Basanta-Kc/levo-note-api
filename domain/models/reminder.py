from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from infrastructure.database import db  
class Reminder(db.Model):
    __tablename__ = 'reminder'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    note_id = Column(db.UUID(as_uuid=True), ForeignKey('note.id'), nullable=False)
    email = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with Note model
    note = relationship("Note", back_populates="reminder")

    def __repr__(self):
        return f"<Reminder {self.id}, Note {self.note_id}, Email {self.email}>"
