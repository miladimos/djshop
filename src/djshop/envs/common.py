import os
import sys
from datetime import timedelta
from pathlib import Path
from django.conf import settings
from os.path import abspath, dirname, join

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = os.path.dirname(__file__)

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATE_DIR = str(BASE_BASE_DIR.joinpath('templates/djshop/'))

sys.path.insert(0, join(PROJECT_ROOT, "apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^q52bhy0%%xi(h9rf4ow=7h*^$8y49+g+ig#8_hx7fnba-i^h*'

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
    'rest_framework_simplejwt',
    'corsheaders',
    'ckeditor',
    "django_unicorn",
    'import_export',
    "debug_toolbar",
    'treebeard',
    'drf_spectacular',

    'apps.accounts',
    'apps.shop',
    'apps.blog',
    'apps.api',
    'apps.pages',
    'apps.payments',
    'apps.friendships',
    'apps.shortener',
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

    # "django.middleware.cache.UpdateCacheMiddleware",
    # "django.middleware.common.CommonMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",

    "debug_toolbar.middleware.DebugToolbarMiddleware",

]

ROOT_URLCONF = 'djshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'djshop.wsgi.application'
ASGI_APPLICATION = 'djshop.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = [str(BASE_BASE_DIR.joinpath('static/djshop/'))]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_REDIRECT_URL = 'home_view'
LOGOUT_REDIRECT_URL = 'home_view'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = 'accounts.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_POST = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 24
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'DJShop API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

CACHES = {
    "default": {
        # "BACKEND": "django.core.cache.backends.redis.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379",

        # "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        # "LOCATION": "c:/foo/bar",

        "BACKEND": "django.core.cache.backends.dummy.DummyCache",

    }
}
