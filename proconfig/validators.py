"""VALIDATORS"""

from functools import wraps
from flask import request

from proconfig.routes.api import error


def validate_spreadsheet_request(func):
    """Validates request being made to pro spreadsheet"""
    @wraps(func)
    def wrapper(*args, **kwargs):

        tech_title = request.view_args.get('tech_title')

        if not tech_title:
            return error(status=400, detail="Must specify a technical title in path")

        return func(*args, **kwargs)
    return wrapper
