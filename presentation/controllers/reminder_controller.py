from flask_smorest import Blueprint
from injector import inject
from domain.schemas import (
    ReminderCreateSchema,
    ReminderSchema,
    PaginationSchema,
    ReminderUpdateSchema,
)
from application.services.reminder_services import ReminderService

reminders_blp = Blueprint("reminders", "reminders", url_prefix="/api/reminders")


# Get all reminders with pagination
@reminders_blp.route("/")
@reminders_blp.arguments(PaginationSchema, location="query")
@inject
def get_reminders(args, reminder_service: ReminderService):
    pagination_data = reminder_service.get_all_reminders(
        args.get("page"), args.get("limit")
    )
    return pagination_data


# Get a single reminder by id
@reminders_blp.route("/<uuid:id>")
@reminders_blp.response(200, ReminderSchema)  # Define the response schema
@inject
def get_reminder(id, reminder_service: ReminderService):
    reminder = reminder_service.get_reminder_by_id(id)
    return reminder


# Create a new reminder
@reminders_blp.route("/", methods=["POST"])
@reminders_blp.arguments(ReminderCreateSchema)
@reminders_blp.response(201)  # Define the response schema
@inject
def create_reminder(data, reminder_service: ReminderService):
    new_reminder = reminder_service.create_reminder(data)
    return {"message": "Reminder created successfully!", "id": new_reminder.id}


# Update an existing reminder
@reminders_blp.route("/<uuid:id>", methods=["PUT"])
@reminders_blp.arguments(ReminderUpdateSchema)
@inject
def update_reminder(data, id, reminder_service: ReminderService):
    reminder_service.update_reminder(id, data)
    return {"message": "Reminder updated successfully!"}


# Delete a reminder
@reminders_blp.route("/<uuid:id>", methods=["DELETE"])
@inject
def delete_reminder(id, reminder_service: ReminderService):
    reminder_service.delete_reminder(id)
    return {"message": "Reminder deleted successfully!", "id": id}
