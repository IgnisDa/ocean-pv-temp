import os

import dj_database_url

from .base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com', '0.0.0.0']

SECRET_KEY = os.environ.get('SECRET_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get('GOOGLE_RECAPTCHA_SECRET_KEY')

GOOGLE_RECAPTCHA_SITE_KEY = os.environ.get('GOOGLE_RECAPTCHA_SITE_KEY')

DATABASE = os.environ.get('DATABASE')

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(DATABASE, conn_max_age=600)
