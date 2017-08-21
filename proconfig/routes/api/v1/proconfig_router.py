"""API ROUTER"""

import logging

from flask import jsonify, Blueprint
from proconfig.routes.api import error
from proconfig.validators import validate_greeting
from proconfig.middleware import set_something
from proconfig.serializers import serialize_greeting
import json
import CTRegisterMicroserviceFlask

proconfig_endpoints = Blueprint('proconfig_endpoints', __name__)


@proconfig_endpoints.route('/hello', strict_slashes=False, methods=['GET'])
@set_something
@validate_greeting
def say_hello(something):
    """World Endpoint"""
    logging.info('[ROUTER]: Say Hello')
    config = {
        'uri': '/dataset',
        'method': 'GET',
    }
    response = CTRegisterMicroserviceFlask.request_to_microservice(config)
    elements = response.get('data', None) or 1
    data = {
        'word': 'hello',
        'propertyTwo': 'random',
        'propertyThree': elements,
        'something': something,
        'elements': 1
    }
    if False:
        return error(status=400, detail='Not valid')
    return jsonify(data=[serialize_greeting(data)]), 200
