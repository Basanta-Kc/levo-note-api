from flask_smorest import Blueprint
from injector import inject
from domain.schemas import ReminderSchema, ReminderIDSchema, PaginationSchema, ReminderUpdateSchema
from flask import jsonify, current_app, request
from application.services.reminder_services import ReminderService

reminders_blp = Blueprint("reminders", "reminders", url_prefix="/reminders")

@reminders_blp.route("/")
@reminders_blp.arguments(PaginationSchema, location="query")
@inject
def get_reminders(args, reminder_service: ReminderService):
    current_app.logger.debug(f"Received arguments: {args}")
    pagination_data = reminder_service.get_all_reminders(args.get('page'), args.get('limit'))
    return jsonify({
            'total': pagination_data['total'],
            'items': [{
                'id': reminder.id,
                'note_id': reminder.note_id,
                'email': reminder.email,
                'date': reminder.date.isoformat(),  # Convert to ISO format
                'created_at': reminder.created_at.isoformat(),
                'updated_at': reminder.updated_at.isoformat()
            } for reminder in pagination_data['items']]
        })

@reminders_blp.route("/<uuid:id>")
@inject
def get_reminder(id, reminder_service: ReminderService):
    reminder = reminder_service.get_reminder_by_id(id)
    return jsonify({
        'id': reminder.id,
        'note_id': reminder.note_id,
        'email': reminder.email,
        'date': reminder.date.isoformat(),
        'created_at': reminder.created_at.isoformat(),
        'updated_at': reminder.updated_at.isoformat()
    })

@reminders_blp.route("/", methods=["POST"])
@reminders_blp.arguments(ReminderSchema)
@inject
def create_reminder(data, reminder_service: ReminderService):
    new_reminder = reminder_service.create_reminder(data)
    return jsonify({'message': 'Reminder created successfully!', 'reminder': {'id': new_reminder.id}}), 201

@reminders_blp.route("/<uuid:id>", methods=["PUT"])
@reminders_blp.arguments(ReminderSchema)
@inject
def update_reminder(data,id, reminder_service: ReminderService):
    reminder_service.update_reminder(id, data)
    return jsonify({'message': 'Reminder updated successfully!'})

@reminders_blp.route("/<uuid:id>", methods=["DELETE"])
@inject
def delete_reminder(id, reminder_service: ReminderService):
    reminder_service.delete_reminder(id)
    return jsonify({'message': 'Reminder deleted successfully!'})
