from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ['testserver']

STATIC_URL = 'https://developers.botify.com/'

MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_DEPLOY_DIR = os.path.join(
    BASE_DIR, '..', "_site"
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
