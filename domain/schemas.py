from marshmallow import Schema, fields, validate

class NoteSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=True, validate=validate.Length(min=1))

class NoteIDSchema(Schema):
    id = fields.UUID(required=True)

class PaginationSchema(Schema):
    page = fields.Integer(missing=1, validate=validate.Range(min=1))
    limit = fields.Integer(missing=10, validate=validate.Range(min=1, max=100))
    search_query = fields.String()

# class ReminderSchema(Schema):
#     note_id = fields.UUID(required=True)
#     email = fields.Email(required=True)
#     date = fields.DateTime(required=True)
#     created_at = fields.DateTime(dump_only=True)
#     updated_at = fields.DateTime(dump_only=True)

class ReminderIDSchema(Schema):
    id = fields.UUID(required=True)

class ReminderUpdateSchema(Schema):
    email = fields.Str(required=True)
    date = fields.DateTime(required=True)


class ReminderSchema(Schema):
    id = fields.UUID()
    email = fields.Str(required=True)
    date = fields.DateTime(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class NoteResponseSchema(Schema):
    id = fields.UUID()
    title = fields.Str(required=True)
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    reminder = fields.Nested(ReminderSchema(only=("id", "email", "date", "created_at", "updated_at")), allow_none=True)

class PaginationResponseSchema(Schema):
    total = fields.Int()
    items = fields.List(fields.Nested(NoteResponseSchema))

