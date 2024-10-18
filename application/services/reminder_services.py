# Reminder Service
from injector import inject
from infrastructure.repositories.reminder_repository import ReminderRepository

class ReminderService:
    @inject
    def __init__(self, reminder_repository: ReminderRepository):
        self.reminder_repository = reminder_repository

    def get_all_reminders(self, page, limit):
        return self.reminder_repository.get_all_reminders(page, limit)

    def get_reminder_by_id(self, reminder_id):
        return self.reminder_repository.get_reminder_by_id(reminder_id)

    def create_reminder(self, data):
        return self.reminder_repository.create_reminder(data)

    def update_reminder(self, reminder_id, data):
        reminder = self.reminder_repository.get_reminder_by_id(reminder_id)
        return self.reminder_repository.update_reminder(reminder, data)

    def delete_reminder(self, reminder_id):
        reminder = self.reminder_repository.get_reminder_by_id(reminder_id)
        self.reminder_repository.delete_reminder(reminder)
