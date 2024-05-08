# schemas.py
"""
This module defines schemas for data validation using Marshmallow. It provides a way to
ensure that incoming data conforms to expected formats before processing.
"""

from marshmallow import Schema, fields, validate

class DataSchema(Schema):
    """
    Schema for validating data related to users.

    Fields:
        name (Str): The name of the user, must be at least 1 character long.
        age (Int): The age of the user, must be a non-negative integer.
    """
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Int(required=True, validate=validate.Range(min=0))
