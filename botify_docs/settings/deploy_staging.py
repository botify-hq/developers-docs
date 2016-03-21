from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ['testserver']

STATIC_URL = 'http://com.botify.saas.staging.developer-docs.s3-website-eu-west-1.amazonaws.com/staticfiles/'

MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_DEPLOY_DIR = os.path.join(
    BASE_DIR, '..', "_site"
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
