from .base import *
from .env import export_envs
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(BASE_DIR))

export_envs(os.path.join(PROJECT_DIR, 'server.env'))

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': 8001
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)