import os

import environ

env = environ.Env(DEBUG=(bool, False))
root = environ.Path(__file__) - 2
environ.Env.read_env()

BASE_DIR = str(root)
SECRET_KEY = 'dfsdfjjd77r93u43ud9id9idkkkcx'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '31.131.17.145']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'database.db',
  }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
