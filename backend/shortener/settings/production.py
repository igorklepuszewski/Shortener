from .base import *
import os

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = False

ROOT_URLCONF = 'shortener.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': 'db',
        'PORT': 5432
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/static'
]

STATIC_ROOT = '/static' #os.path.join(BASE_DIR, 'staticfiles')