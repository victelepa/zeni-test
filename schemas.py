# schemas.py
from marshmallow import Schema, fields, validate

class DataSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Int(required=True, validate=validate.Range(min=0))
