#!/usr/bin/python3
'''Contains a Flask web appplication API.
'''
import os
from flask import Flask, jsonify
from flask_cors import CORS

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
'''The Flask web application instance.'''
app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
# enable CORS and allow for origins:
CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def teardown_engine(exception):
    '''The Flask app/request context end event listener.'''
    # print(exception)
    storage.close()


# Error handlers for expected app behavior:
@app.errorhandler(404)
def not_found(error):
    '''Handles the 404 HTTP error code.'''
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(
        host=app_host,
        port=app_port,
        threaded=True
    )
