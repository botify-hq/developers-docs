"""
Django settings for botify_docs project on Heroku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.realpath(
    os.path.join(os.path.abspath(__file__), '../..')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "%sqdqdxr6=0!(!)@j%=c+@1u#e#11+1j)at1-chy#orfk0^vvk"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_medusa',
    'api_docs',
    'botify_docs',
    'pipeline',
    'storages'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'botify_docs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'botify_docs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Enable Persistent Connections
DATABASES['default']['CONN_MAX_AGE'] = 500

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = '_site/staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'botify_docs.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder'
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


MEDUSA_RENDERER_CLASS = "django_medusa.renderers.S3StaticSiteRenderer"
MEDUSA_MULTITHREAD = False
MEDUSA_COLLECT_STATIC = False
FINDER_IGNORE_PATTERNS = [
    '*.scss',
    '*.scssc',
    '*.less',
    'node_modules',
    'examples',
    'unit_testing',
    'tests',
    'test',
]

# @TODO use the prod's real urls once they are released
SWAGGER_API_URL = "https://api.botify.com/v1/swagger.json"
DATAMODEL_API_URL = "https://api.botify.com/v1/analyses/datamodel"


PIPELINE = {
    'STYLESHEETS': {
        'swagger_ui': {
            'source_filenames': (
                'swagger-ui/dist/css/typography.css',
                'swagger-ui/dist/css/screen.css'
            ),
            'output_filename': 'css/style_swagger.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
        'main_style': {
            'source_filenames': (
                'style/css/bootstrap.min.css',
                'style/css/main.css',
            ),
            'output_filename': 'css/style_main.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
        'common_style': {
            'source_filenames': (
                'style/css/monokai-sublime.css',
                'style/css/bootstrap.min.css',
                'style/css/datatables.min.css',
                'style/css/common.css',
            ),
            'output_filename': 'css/style_common.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'swagger_ui': {
            'source_filenames': (
                'js/jquery/jquery.min.js',
                'js/jquery/jquery-migrate-1.3.0.min.js',
                'js/bootstrap/bootstrap.min.js',
                'swagger-ui/dist/lib/jquery.slideto.min.js',
                'swagger-ui/dist/lib/jquery.wiggle.min.js',
                'swagger-ui/dist/lib/jquery.ba-bbq.min.js',
                'swagger-ui/dist/lib/handlebars-2.0.0.js',
                'swagger-ui/dist/lib/js-yaml.min.js',
                'swagger-ui/dist/lib/lodash.min.js',
                'swagger-ui/dist/lib/backbone-min.js',
                'swagger-ui/dist/swagger-ui.js',
                'js/highlight/highlight.pack.js',
                'swagger-ui/dist/lib/jsoneditor.min.js',
                'swagger-ui/dist/lib/marked.js',
                'swagger-ui/dist/lib/swagger-oauth.js'
            ),
            'output_filename': 'js/script_swagger.js',
        },
        'common_script': {
            'source_filenames': (
                'js/highlight/highlight.pack.js',
                'js/jquery/jquery.min.js',
                'js/jquery/url.min.js',
                'js/bootstrap/bootstrap.min.js',
                'js/datatables/datatables.min.js',
            ),
            'output_filename': 'js/script_common.js',
        }
    }
}

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'

REDIRECTS = (
    ('api/usage/aggregate-urls/', '/api/analysis/aggregate-urls/'),
    ('api/usage/csv-export/', '/api/analysis/csv-export/'),
    ('api/usage/get-url-detail/', '/api/analysis/get-url-detail/'),
    ('api/usage/list-analyses/', '/api/analysis/list-analyses/'),
    ('api/usage/query-urls/', '/api/analysis/search-for-urls/'),
    ('api/usage/list-projects/', '/api/project/list-projects/'),
)
