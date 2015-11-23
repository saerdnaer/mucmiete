from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z8ihu+ksnt+y9jy1*q&tglhs8#8+(8^70p==^w!1_*bny_+(j*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '::1']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# support proxy for debugging
# in nginx set:
# proxy_set_header X-Forwarded-Proto $scheme;
# proxy_set_header X-Forwarded-Host $host;
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST= True

STATIC_ROOT = os.path.join(BASE_DIR, 'static.deploy')
