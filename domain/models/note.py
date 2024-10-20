from datetime import datetime, timezone
from sqlalchemy.orm import relationship
import uuid
from infrastructure.database import db


class Note(db.Model):
    __tablename__ = "note"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    reminder = relationship(
        "Reminder", back_populates="note", uselist=False, cascade="all, delete-orphan"
    )
