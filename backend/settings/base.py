# -*- coding: utf-8 -*-

from os import path, mkdir
import re


# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.normpath(path.join(path.dirname(__file__), '../..'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#+xpex37k%yn5xjrbb_7=80ed2o1ysdlkp7&(m*7ucx3r7h#1b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


CORS_ORIGIN_WHITELIST = []

# Application component definitions

PROJECT_APPS = [
    'core',
    'users',
]
LIBRARY_APPS = [
    'rest_framework',
    'django_extensions',
]
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
DEBUG_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS = PROJECT_APPS + LIBRARY_APPS + DJANGO_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(BASE_DIR, 'backend/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#######################
# Database
#######################

# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': '',
#         'USER': 'postgres',
#     }
# }


#######################
# Password validation
#######################

# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#######################
# Static files (CSS, JavaScript, Images)
#######################
STATIC_ROOT = path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

#######################
# Internationalization
#######################

# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-au'
TIME_ZONE = 'Australia/Sydney'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Customer user model
AUTH_USER_MODEL = 'users.User'

JWT_AUTHENTICATION = {

    # The length of time for which the token is valid
    'TIMEOUT_MINUTES': 60 * 36,

    # This specifies how often the keepalive event is triggered
    'KEEPALIVE_INTERVAL_MINUTES': 2,

    # The amount of time the user has to respond before they have been
    # considered timed out. Set to 0 or false to disable this feature, if you want
    # Idle to nothing but detect when a user is idle or not forever.
    'USER_TIMEOUT_DURATION_MINUTES': 0,

    # The idle timeout duration. After this amount of time passes without
    # the user performing an action that triggers one of the watched DOM events, the
    # user is considered idle. Note: Prior to v1.0, this method is called idleDuration.
    'USER_IDLE_DURATION_MINUTES': 10,
}


# Load local settings

try:
    from local import *
except ImportError:
    pass
except IOError:
    pass

if DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + DEBUG_APPS

# Logging

# Define the path where log files are written
LOG_PATH = path.join(BASE_DIR, 'logs/')
if not path.isdir(LOG_PATH):
    mkdir(LOG_PATH)

# Ignore all default logging
LOGGING_CONFIG = None

# The default error level handler
LOGGING_DEFAULT_ERROR = {
    'django': {
        'handlers':['errorfile'],
        'propagate': True,
        'level':'ERROR',
    },
}

# Check if any loggers have been defined in local.py
try:
    LOGGERS.update(LOGGING_DEFAULT_ERROR)
except NameError:
    LOGGERS = LOGGING_DEFAULT_ERROR


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            # 'filename': path.join(LOG_PATH, 'django.log'),
            'formatter': 'verbose'
        },
        'errorfile': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': path.join(LOG_PATH, 'django.log'),
            'formatter': 'verbose'
        },
        'infofile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': path.join(LOG_PATH, 'app.log'),
            'formatter': 'verbose'
        },
        'debugfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOG_PATH, 'debug.log'),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 *2,  # File size is 2M
            'backupCount': 10,       # Keep 100 files
        },
    },
    'loggers': LOGGERS
}


import logging.config
logging.config.dictConfig(LOGGING)
