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
