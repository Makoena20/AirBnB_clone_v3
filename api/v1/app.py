#!/usr/bin/python3
"""
This module starts the Flask web application and handles all routing and CORS setup.
"""

from flask import Flask, jsonify
from flask_cors import CORS

# Create an instance of the Flask class
app = Flask(__name__)

# Enable CORS on all routes and origins
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.route('/api/v1/states/<state_id>/cities/<city_id>', methods=['GET'])
def get_city(state_id, city_id):
    """ Retrieve a city based on its state and city IDs """
    # Example response, you should replace it with your actual data retrieval logic
    city = {
        "__class__": "City",
        "created_at": "2017-03-25T02:17:06",
        "id": "1da255c0-f023-4779-8134-2b1b40f87683",
        "name": "New Orleans",
        "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd",
        "updated_at": "2017-03-25T02:17:06"
    }
    return jsonify(city)

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)

