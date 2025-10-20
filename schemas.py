from marshmallow import Schema, fields


class CoordinatesSchema(Schema):
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)


class LocationSchema(Schema):
    name = fields.String(required=True)
    coordinates = fields.Nested(CoordinatesSchema)


class CatchSchema(Schema):
    species = fields.String(required=True)
    weight_kg = fields.Float(required=True)
    length_cm = fields.Float(required=True)
    time = fields.String(required=True)


class SessionSchema(Schema):
    session_id = fields.String(required=True)
    date = fields.String(required=True)
    location = fields.Nested(LocationSchema, required=True)
    fishing_rods = fields.Integer(required=True)
    bait = fields.List(fields.String(), required=True)
    catches = fields.List(fields.Nested(CatchSchema), required=True)
    notes = fields.String()


session_schema = SessionSchema()
