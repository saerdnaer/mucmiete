from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '::1']


HTTPS_SUPPORT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
