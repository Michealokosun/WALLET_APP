#!/usr/bin/env python

"""
flask app for api calls
"""

from datetime import timedelta
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from models import storage
from api.views import app_views
from os import getenv
from models import storage
from models.user import User


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.errorhandler(404)
def not_found(error):
    """custom 404 error message"""
    return jsonify({"Error": "The requested resource could not be found"}), 404

@app.errorhandler(401)
def unauthorized(error):
    """custom 401 error message"""
    return jsonify({"Error": "You are not authorized to access this resource"}), 401


@app.route('/', methods=['GET'])
def home():
    """home route"""
    return jsonify({"message": "Welcome to the MY WALLET API"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
