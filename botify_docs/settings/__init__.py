import os

BOTIFY_ENVIRONMENT = os.getenv('BOTIFY_ENVIRONMENT')

if BOTIFY_ENVIRONMENT == 'local':
    from .local import *  # NOQA
else:
    from .base import *  # NOQA
