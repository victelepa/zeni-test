from flask import Flask, request, jsonify
from datetime import datetime
from marshmallow import Schema, fields, validate, ValidationError

class DataSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Int(required=True, validate=validate.Range(min=0))

app = Flask(__name__)
schema = DataSchema()

@app.route('/')
def welcome():
    return "Welcome to the API"

@app.route('/data', methods=['POST'])
def post_data():
    if request.is_json:
        try:
            data = schema.load(request.get_json())
            data['timestamp'] = datetime.utcnow().isoformat() + 'Z'
            return jsonify(data), 200
        except ValidationError as err:
            return jsonify(err.messages), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
