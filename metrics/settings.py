"""
Django settings for this project
"""
import os
from rpg.util.configurator import Configurator


PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
WORKSPACE = os.path.abspath(os.path.join(PROJECT_PATH, "../"))
CONFIG = Configurator(PROJECT_PATH)

DEBUG = CONFIG.debug # SECURITY WARNING: don't run with debug turned on in production!
TEMPLATE_DEBUG = CONFIG.debug
ALLOWED_HOSTS = CONFIG.get("ALLOWED_HOSTS", ["*"])
ADMINS = CONFIG.get("ADMINS", [])
EXTERNAL_REQUEST_TIMEOUT = float(CONFIG.get('EXTERNAL_REQUEST_TIMEOUT'))
SECRET_KEY = CONFIG.secret_key

URI = CONFIG.get("URI")
if URI.endswith("/"):
    URI = URI[0:len(URI) - 1]

NEWRELIC = CONFIG.get("NEWRELIC", False)
# if LOCAL_MODE is False and config.contains("LOGGING"):
#     LOGGING = config.get("LOGGING")


IMAGE_SIZES = CONFIG.get("IMAGE_SIZES")

# Application definition
ROOT_URLCONF = 'metrics.urls'
WSGI_APPLICATION = 'metrics.wsgi.application'

# Databases - https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = CONFIG.get("DATABASES")
SOUTH_DATABASE_ADAPTERS = {
    'default': "south.db.postgresql_psycopg2"
}

# Internationalization - https://docs.djangoproject. com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ENABLE CROSS SITE STUFF
CORS_ORIGIN_ALLOW_ALL = True

# Static files (CSS, JavaScript, Images) - https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# # POINT TO THE FIXTURES SUBDIRECTORY
# FIXTURE_DIRS = (
#     os.path.abspath(os.path.join(PROJECT_PATH, "../rpg/migrations/fixtures")),
# )


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'corsheaders',
    'rpg'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "metrics.middleware.attach_values",
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'metrics.middleware.ErrorHandler'
)

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
#     'PAGINATE_BY': 50,
#     'PAGINATE_BY_PARAM': 'page_size',
#     'MAX_PAGINATE_BY': 100,
#     #'EXCEPTION_HANDLER': 'balance.global_exception_handler'
# }
