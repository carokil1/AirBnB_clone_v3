#!/usr/bin/python3
"""define the router of the app_views blueprint"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def api_status():
    """return the status of the app
    """
    response = {'status': 'OK'}
    return jsonify(response)
