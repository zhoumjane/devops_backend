"""
Django settings for devops_backend project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, sys
import uuid
import datetime
from django.core.files.storage import Storage

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR, "apps"))
TMP_DIR = os.path.join(BASE_DIR, 'tmp')

if not os.path.isdir(TMP_DIR):
    os.makedirs(TMP_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$=yx52b9=d^86h(8k5#p%9%xax5br0!(#1b+2prlm53#f%yspz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'celery',
    'channels',
    'django_celery_results',
    'users.apps.UsersConfig',
    'groups.apps.GroupsConfig',
    'servers.apps.ServersConfig',
    'images.apps.ImagesConfig',
    'sshchan.apps.SshchanConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ASGI_APPLICATION = 'sshchan.urls.application'

ROOT_URLCONF = 'devops_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'devops_backend.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devops',
        'USER': 'root',
        'PASSWORD': 'zmj930826',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS':{
            'init_command': 'SET default_storage_engine=INNODB;',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

AUTHENTICATION_BACKENDS = (
    'utils.auth.CustomBackend',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_all')
STATIC_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')


# celery settings

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['application/json',]
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_MAX_TASKS_PER_CHILD = 1000
IMAGE_PUSH_HOST = "172.20.52.55"
DIR_PATH = "/data/"


#email
EMAIL_HOST = 'zhoumjane@163.com'
EMAIL_PORT = 587
EMAIL_TO = 'zhoumjane@163.com'
EMAIL_HOST_PASSWORD = 'zhoumjane@163.com'
EMAIL_USE_SSL = False
EMAIL_FROM = 'zhoumjane@163.com'
DOMAIN = "@163.com"

# redis cache settings

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
REST_FRAMEWORK_EXTENSIONS = {
    "DEFAULT_CACHE_RESPONSE_TIMEOUT": 1
}

# redis lock settings

HOST_PATH = '/etc/hosts'
HOST_PATH_SRC = '/etc/hosts_src'
HOST_PATH_IMAGE = '/etc/hosts_image'
UUID_TOKEN = uuid.uuid4()
REDIS_HOST = 'localhost'
REDIS_PORT = 6379


# config cors settings

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*',
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW'
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
    'x-token',
    'TOKEN',
    'Access-Control-Allow-Origin'
)


# jwt settings

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=86400),
    'JWT_AUTH_HEADER_PREFIX': "TOKEN",
}


# sso jwt settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'utils.sso_auth.authentication.SSOJSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user': '200/minute',
        'anon': '100/minute'
    }
}
