# auth.py
"""
This module configures authentication for the Flask application using Flask-HTTPAuth.
It provides mechanisms to verify user credentials and handle authentication errors.
"""

from flask_httpauth import HTTPBasicAuth
from flask import g, jsonify

auth = HTTPBasicAuth()

users = {
    "admin": {"password": "secret", "role": "admin"},
    "user": {"password": "password", "role": "user"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify the provided username and password.

    Parameters:
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        bool: True if the username and password are correct, otherwise False.
    """
    user = users.get(username)
    if user and user['password'] == password:
        g.user = user
        return username

@auth.error_handler
def auth_error(status):
    """
    Handle authentication errors by returning a JSON response.

    Parameters:
        status (int): HTTP status code to return in the error response.

    Returns:
        Response: JSON response containing an error message.
    """
    return jsonify({"error": "Access denied, invalid credentials or insufficient permissions"}), status
