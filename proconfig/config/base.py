"""-"""

import os

SETTINGS = {
    'logging': {
        'level': 'DEBUG'
    },
    'service': {
        'port': os.getenv('PORT'),
        'name': 'GS PRO Text Configuration'
    }
}
