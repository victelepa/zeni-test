# app.py
import os
from flask import Flask, request, jsonify, g
from datetime import datetime
from functools import wraps
from marshmallow import ValidationError

from schemas import DataSchema
from auth import auth, auth_error
from config import DevelopmentConfig, ProductionConfig, TestingConfig


app = Flask(__name__)
schema = DataSchema()

print("Current FLASK_ENV:", os.getenv('FLASK_ENV'))

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object(ProductionConfig())
    print("production mode")
elif os.getenv('FLASK_ENV') == 'testing':
    app.config.from_object(TestingConfig())
    print("testing mode")
elif os.getenv('FLASK_ENV') == 'development':
    app.config.from_object(DevelopmentConfig())
    print("dev mode")

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if g.user['role'] != role:
                return jsonify({"error": "Access denied. Admin required."}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/')
@auth.login_required
def welcome():
    return "Welcome to the API"

@app.route('/data', methods=['POST'])
@auth.login_required
@role_required('admin')
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
