"""Incident schema."""

import marshmallow

fields = marshmallow.fields


class IncidentSchema(marshmallow.Schema):

    phone_number = fields.String()
    location = fields.Dict()
    emergency_type = fields.String()
    status = fields.String()
    created_time = fields.DateTime()
