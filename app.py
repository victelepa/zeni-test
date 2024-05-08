# app.py
"""
This module initializes the Flask application and its routes. It configures the application based
on the environment and applies role-based access control to certain endpoints.
"""
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
    """
    Decorator to enforce role-based access control for routes.

    Parameters:
        role (str): The role required to access the function.

    Returns:
        function: The decorator that checks user's role before executing the function.
    """
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
    """Returns a welcome message to the authenticated user."""
    return "Welcome to the API"

@app.route('/data', methods=['POST'])
@auth.login_required
@role_required('admin')
def post_data():
    """
    Processes JSON data from the request by adding a timestamp and returning it.
    Only accessible by users with the 'admin' role.

    Returns:
        Response: JSON data with a timestamp or an error message.
    """
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
