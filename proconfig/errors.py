"""ERRORS"""


class Error(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code

    @property
    def serialize(self):
        return {
            'message': self.message,
            'code': self.code
        }
