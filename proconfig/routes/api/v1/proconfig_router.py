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

    logging.info('[ROUTER]: print spreadsheet')

    #get data from speadsheet using Googlesheet util
    try:
        data = GoogleSheet.sheet_to_dict('Form Responses', tech_title)
    except Exception as e:
        logging.error('[ROUTER]: '+str(e))
        return error(status=500, detail=e.message)

    return jsonify({'data': data}), 200
