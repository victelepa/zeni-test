from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the API"

@app.route('/data', methods=['POST'])
def post_data():
    if request.is_json:
        data = request.get_json()
        data['timestamp'] = datetime.utcnow().isoformat() + 'Z'
        return jsonify(data), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
