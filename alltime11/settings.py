"""
Django settings for alltime11 project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import sys
import os
import pathlib
from pathlib import Path
from datetime import timedelta

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# load .env file
env = environ.Env()
environ.Env.read_env(pathlib.PurePath(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

BASE_URL = env.str('BASE_URL')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ENVIRONMENT = env.str("environment", default="dev")

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'corsheaders',
    'rest_framework',
    'phonenumber_field',
    'users',
    'cricket',
    'common_api',
]

# TODO: update this when going live
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:4444",
#     "https://alltime11.com",
#     "http://alltime11.com",
# ]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'alltime11.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alltime11.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL')
}

CACHES = {
    'default': env.cache('REDIS_CACHE_URL')
}

if 'test' in sys.argv:
    CACHES['default'] = env.cache('TEST_REDIS_CACHE_URL')

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'alltime11.auth.AllTimeAuthentication',
    ),
    "DEFAULT_PERMISSION_CLASSES": ('rest_framework.permissions.IsAuthenticated',)
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'UPDATE_LAST_LOGIN': True,
}

CELERY_TASK_QUEUES = {
    'high': {
        'exchange': 'high',
        'routing_key': 'high',
    },
    'mid': {
        'exchange': 'mid',
        'routing_key': 'mid',
    },
    'low': {
        'exchange': 'low',
        'routing_key': 'low',
    },
}

CELERY_TASK_CREATE_MISSING_QUEUES = True

DJANGO_LOG_LEVEL = env.str('DJANGO_LOG_LEVEL', default='INFO')
LOG_LEVEL = env.str('LOG_LEVEL', default='INFO')
LOGGING_DIR = Path.joinpath(BASE_DIR, 'logs')
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {name} {pathname} {lineno:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "api": {
            "level": LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": Path.joinpath(LOGGING_DIR, 'api.log'),
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
        },
        "high": {
            "level": LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": Path.joinpath(LOGGING_DIR, 'high.log'),
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
        },
        "mid": {
            "level": LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": Path.joinpath(LOGGING_DIR, 'mid.log'),
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
        },
        "low": {
            "level": LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": Path.joinpath(LOGGING_DIR, 'low.log'),
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": DJANGO_LOG_LEVEL,
            "propagate": False,
        },
        "api": {
            "handlers": ["api"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        'celery.high': {
            'handlers': ['high'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'celery.mid': {
            'handlers': ['mid'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'celery.low': {
            'handlers': ['low'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },
}

if DEBUG:
    LOGGING["loggers"]["api"]["handlers"].append("console")
    LOGGING["loggers"]["celery.high"]["handlers"].append("console")
    LOGGING["loggers"]["celery.mid"]["handlers"].append("console")
    LOGGING["loggers"]["celery.low"]["handlers"].append("console")


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

PHONENUMBER_DEFAULT_REGION = 'IN'

# ROUNAZ
ROUNAZ_API_KEY = env.str('ROUNAZ_API_KEY')
ROUNAZ_PROJECT_KEY = env.str('ROUNAZ_PROJECT_KEY')
ROUNAZ_BASE_URL = env.str('ROUNAZ_BASE_URL')

# CELERY
CELERY_RESULT_BACKEND = CELERY_BROKER_URL = env.str('REDIS_CELERY_URL')
ADMIN_USER_ID = env.int("ADMIN_USER_ID")

# AWS
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
AWS_REGION = env.str('AWS_REGION')
ATTACHMENT_BUCKET = env.str('ATTACHMENT_BUCKET')

# FIREBASE
FIREBASE_BASE_URL = env.str('FIREBASE_BASE_URL')
FIREBASE_PROJECT_ID = env.str('FIREBASE_PROJECT_ID')
FIREBASE_SCOPE_URL = env.str('FIREBASE_SCOPE_URL')
FIREBASE_SERVICE_ACCOUNT_FILE = env.str('FIREBASE_SERVICE_ACCOUNT_FILE')

# SMSCOUNTRY
SMS_COUNTRY_AUTH_KEY = env.str('SMS_COUNTRY_AUTH_KEY')
SMS_COUNTRY_AUTH_TOKEN = env.str('SMS_COUNTRY_AUTH_TOKEN')
SMS_COUNTRY_SENDER_ID = env.str('SMS_COUNTRY_SENDER_ID')
SMS_COUNTRY_API_URL = env.str('SMS_COUNTRY_API_URL')
