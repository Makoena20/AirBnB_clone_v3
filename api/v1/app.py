#!/usr/bin/python3
"""
Flask App that integrates with SQLAlchemy ORM
"""
from flask import Flask, jsonify, abort
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db(error):
    """
    After each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session.
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    """
    Main function
    """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
