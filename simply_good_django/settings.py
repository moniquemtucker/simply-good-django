"""
Django settings for simply_good_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# just added paths
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '+5x_5z#@ypk$lw9lxz@^lwxelfe_m5kwaeog#8^3$pc=(m$_=m'
SECRET_KEY = os.environ["SIMPLYGOOD"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [os.environ.get('.herokuapp.com')]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'crispy_forms',
    # 'signups',
    # 'person',
    'diary',
    'userprofile',
    'chartkick',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simply_good_django.urls'

WSGI_APPLICATION = 'simply_good_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sg49db',
        'USER': 'momo',
        'PASSWORD': 'changeme!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

try:
    if 'DATABASE_URL' in os.environ:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])

        # Update with environment configuration
        DATABASES['default'].update({
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        })
except Exception:
    print 'Unexpected error configuring database:', sys.exc_info()

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
import chartkick
STATICFILES_DIRS = (
    STATIC_PATH,
    chartkick.js(),
)

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

CRISPY_TEMPLATE_PACK = 'bootstrap'