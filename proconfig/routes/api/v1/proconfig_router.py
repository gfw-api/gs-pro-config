"""Pro API ROUTER"""

import logging
import json
from flask import jsonify, Blueprint

from proconfig.routes.api import error
from proconfig.validators import validate_spreadsheet_request
from proconfig.middleware import set_something
from proconfig.serializers import serialize_greeting
from proconfig.utils import GoogleSheet
import CTRegisterMicroserviceFlask

proconfig_endpoints = Blueprint('proconfig_endpoints', __name__)


@proconfig_endpoints.route('/pro-config/<tech_title>', strict_slashes=False, methods=['GET'])
@validate_spreadsheet_request

def get_spreadsheet(tech_title):
    """Spreadsheet Endpoint"""
    #Next Step add a rebuild cache
    logging.info('[ROUTER]: print spreadsheet')

    data = GoogleSheet.sheet_to_dict('Form Responses', tech_title)

    return jsonify({'data': data}), 200
