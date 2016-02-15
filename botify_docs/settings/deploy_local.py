from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ['testserver']

STATIC_URL = '/staticfiles/'

MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_DEPLOY_DIR = os.path.join(
    BASE_DIR, '..', "_output"
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
