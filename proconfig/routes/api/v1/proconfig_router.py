import logging

from flask import jsonify, Blueprint

from proconfig.routes.api import error
from proconfig.utils import GoogleSheet
from proconfig.validators import validate_spreadsheet_request
from gspread.exceptions import APIError

proconfig_endpoints = Blueprint('proconfig_endpoints', __name__)


@proconfig_endpoints.route('/<tech_title>', strict_slashes=False, methods=['GET'])
@validate_spreadsheet_request
def get_spreadsheet(tech_title):
    """Spreadsheet Endpoint"""

    logging.info('[ROUTER]: print spreadsheet')

    # get data from spreadsheet using Google Sheets util
    try:
        data = GoogleSheet.sheet_to_dict('Form Responses', tech_title)
    except APIError as e:
        logging.error('[ROUTER]: ' + str(e))
        if e.args[0]['status'] == 'RESOURCE_EXHAUSTED':
            return error(status=500, detail='Google sheets query quota exhausted')
        status_code = e.code if e.code is not None else 500
        return error(status=status_code, detail=e.message)
    except Exception as e:
        logging.error('[ROUTER]: ' + str(e))
        status_code = e.code if e.code is not None else 500
        return error(status=status_code, detail=e.message)

    return jsonify({'data': data}), 200
