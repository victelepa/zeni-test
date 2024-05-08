# test_app.py
import sys
import os
import pytest

# Add the root directory to the PYTHONPATH so that 'app' can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from app import app as flask_app  # import the Flask app from app.py

@pytest.fixture
def app():
    app = flask_app
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_welcome(client):
    """Test the welcome route with admin credentials."""
    response = client.get('/', headers={"Authorization": "Basic YWRtaW46c2VjcmV0"})  # admin:secret base64 encoded
    assert response.status_code == 200
    assert response.data == b'Welcome to the API'

def test_post_data(client):
    """Test the post data route with admin credentials."""
    data = {
        'name': 'John',
        'age': 31
    }
    headers = {
        "Authorization": "Basic YWRtaW46c2VjcmV0"  # admin:secret base64 encoded
    }
    response = client.post('/data', json=data, headers=headers)
    assert response.status_code == 200
    assert 'name' in response.json and response.json['name'] == 'John'
    assert 'age' in response.json and response.json['age'] == 31
    assert 'timestamp' in response.json


