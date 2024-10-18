# Reminder Service
from flask_mail import Message
from application.services.email_services import send_email
from mail import mail
from scheduler_config import scheduler
from apscheduler.triggers.date import DateTrigger
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

    def print_reminder(self, email):
        print(email)

    
        
    def create_reminder(self, data):
        reminder = self.reminder_repository.create_reminder(data)
        send_email(reminder.email)
        scheduler.add_job(
            func=send_email,
            trigger=DateTrigger(run_date=reminder.date),
            id=str(reminder.id),
            args=[reminder.email],
            replace_existing=True  # Replace if job already exists
        )
        return reminder

    def update_reminder(self, reminder_id, data):
        reminder = self.reminder_repository.get_reminder_by_id(reminder_id)
        updatedReminder = self.reminder_repository.update_reminder(reminder, data)
        # Remove existing job and add new one
        # since modiying_job didn't work as expected
        scheduler.remove_job(str(reminder.id))
        scheduler.add_job(
            func=self.print_reminder,
            trigger=DateTrigger(run_date=updatedReminder.date),
            id=str(reminder_id),
            args=[reminder.email],
            replace_existing=True  # Replace if job already exists
        )
        return updatedReminder

    def delete_reminder(self, reminder_id):
        reminder = self.reminder_repository.get_reminder_by_id(reminder_id)
        scheduler.remove_job(str(reminder.id))
        self.reminder_repository.delete_reminder(reminder)
