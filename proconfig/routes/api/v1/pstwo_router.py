"""API ROUTER"""

import logging

from flask import jsonify, Blueprint
from proconfig.routes.api import error
from proconfig.validators import validate_greeting
from proconfig.middleware import set_something
from proconfig.serializers import serialize_greeting

pstwo_endpoints = Blueprint('pstwo_endpoints', __name__)


@pstwo_endpoints.route('/hello', strict_slashes=False, methods=['GET'])
@set_something
@validate_greeting
def say_hello(something):
    """World Endpoint"""
    logging.info('[ROUTER]: Say Hello')
    data = {
        'word': 'hello2',
        'propertyTwo': 'random2',
        'propertyThree': 'value2',
        'something': something
    }
    if False:
        return error(status=400, detail='Not valid')
    return jsonify(data=[serialize_greeting(data)]), 200
