# Reminder Service
from flask import render_template
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

    def create_reminder(self, data):
        """
        Creates a new reminder and schedules an email to be sent to the specified email address 
        at the specified date.

        Args:
            data (dict): A dictionary containing the reminder data.

        Returns:
            Reminder: The created reminder object.
        """
        reminder = self.reminder_repository.create_reminder(data)
        scheduler.add_job(
            func=send_email,
            trigger=DateTrigger(run_date=reminder.date),
            id=str(reminder.id),
            args=[
                reminder.email,
                "Levo Note Reminder",
                render_template("email_template.html", note_id=reminder.note.id),
            ],
            replace_existing=True,  
        )
        return reminder

    def update_reminder(self, reminder_id, data):
        reminder = self.reminder_repository.get_reminder_by_id(reminder_id)
        updatedReminder = self.reminder_repository.update_reminder(reminder, data)

        job = scheduler.get_job(str(reminder.id))
        if job:
            scheduler.reschedule_job(
                job_id=str(reminder.id),
                trigger=DateTrigger(run_date=updatedReminder.date),
            )
        else:
            scheduler.add_job(
                func=send_email,
                trigger=DateTrigger(run_date=updatedReminder.date),
                id=str(reminder_id),
                args=[
                    reminder.email,
                    "Levo Note Reminder",
                    render_template("email_template.html", note_id=reminder.note.id),
                ],
                replace_existing=True, 
            )
        return updatedReminder

    def delete_reminder(self, reminder_id):
        reminder = self.reminder_repository.get_reminder_by_id(reminder_id)
        scheduler.remove_job(str(reminder.id))
        self.reminder_repository.delete_reminder(reminder)
