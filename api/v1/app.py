#!/usr/bin/python3
"""
This module creates a Flask instance and sets up the API with CORS enabled.
"""

from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)

# Set up CORS to allow all origins
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)

