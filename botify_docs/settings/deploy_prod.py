from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ['testserver']

STATIC_URL = 'https://developers.botify.com/'

STATICFILES_STORAGE = 'botify_docs.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'botify_docs.storage.MediaFilesStorage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', None)
AWS_ACCESS_KEY = AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
AWS_STORAGE_BUCKET_NAME = 'com.botify.saas.production.developer-docs'
