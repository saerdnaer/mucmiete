from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z8ihu+ksnt+y9jy1*q&tglhs8#8+(8^70p==^w!1_*bny_+(j*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

HTTPS_SUPPORT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
