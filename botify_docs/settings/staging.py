from .base import *  # NOQA

DEBUG = False

# This variable is needed otherwise django-medusa
# renderers don't work (403 with DEBUG=False):
ALLOWED_HOSTS = ['testserver']

STATIC_URL = '/staticfiles/'
