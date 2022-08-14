import os

import environ

env = environ.Env(DEBUG=(bool, False))
root = environ.Path(__file__) - 2
environ.Env.read_env()

BASE_DIR = str(root)
SECRET_KEY = env.str('SECRET_KEY', '!!! SET YOUR SECRET_KEY !!!')

DEBUG = env.bool('DEBUG', True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'database.db',
  }
}
