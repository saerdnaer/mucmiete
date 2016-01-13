"""
Django settings for miete project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from .preconfig import *

try:
    from .plz_mapping import *
except:
    logging.getLogger(__name__).error('You need to create "settings/plz_mapping.py" by running `./manage.py create_plz_mapping`.')

# Application definition

if HAVE_ADMIN:
    ADMIN_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django_admin_bootstrapped',
        'django.contrib.admin',
        'django.contrib.admindocs',
    )
    ADMIN_MIDDLEWARE = (
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    )
    ADMIN_CONTEXTPROC = ['django.contrib.auth.context_processors.auth']
else:
    ADMIN_APPS = ()
    ADMIN_MIDDLEWARE = ()
    ADMIN_CONTEXTPROC = []

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'captcha',
) + ADMIN_APPS + (
    'miete',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
) + ADMIN_MIDDLEWARE + (
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ] + ADMIN_CONTEXTPROC + [
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'de-de'
LANGUAGES = (
    ('en', 'English'),
    ('de', 'Deutsch'),
)

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    #    '/var/www/static/',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# addon packages

# No Captcha reCaptcha
NOCAPTCHA = True

BOOTSTRAP3 = {
    # The URL to the jQuery JavaScript file
    'jquery_url': '/static_jquery/js/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '/static/bootstrap/',
}
