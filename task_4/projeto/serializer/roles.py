from marshmallow import (
    Schema,
    fields
)
class RolesSchema(Schema):

    description = fields.Str()
