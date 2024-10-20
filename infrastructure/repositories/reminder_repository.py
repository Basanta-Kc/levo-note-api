from domain import Reminder
from infrastructure.database import db


class ReminderRepository:
    def get_all_reminders(self, page, limit):
        # Get paginated reminders
        pagination = Reminder.query.paginate(page=page, per_page=limit)

        return {"total": pagination.total, "items": pagination.items}

    def get_reminder_by_id(self, reminder_id):
        return Reminder.query.get_or_404(reminder_id)

    def create_reminder(self, data):
        new_reminder = Reminder(**data)
        db.session.add(new_reminder)
        db.session.commit()
        return new_reminder

    def update_reminder(self, reminder, data):
        reminder.note_id = data.get("note_id", reminder.note_id)
        reminder.email = data.get("email", reminder.email)
        reminder.date = data.get("date", reminder.date)
        db.session.commit()
        return reminder

    def delete_reminder(self, reminder):
        db.session.delete(reminder)
        db.session.commit()
