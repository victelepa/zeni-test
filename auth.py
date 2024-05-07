# auth.py
from flask_httpauth import HTTPBasicAuth
from flask import g, jsonify

auth = HTTPBasicAuth()

users = {
    "admin": {"password": "secret", "role": "admin"},
    "user": {"password": "password", "role": "user"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        g.user = user
        return username

@auth.error_handler
def auth_error(status):
    return jsonify({"error": "Access denied, invalid credentials or insufficient permissions"}), status
