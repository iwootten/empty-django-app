from djempty.settings.base import *

import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')