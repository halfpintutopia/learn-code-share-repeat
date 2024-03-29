"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta

import os
import dj_database_url

if os.path.exists(find_dotenv()):
    load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "users/templates")
ROOT_DIR = BASE_DIR.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=0))

# Disable the Browsable API in production
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DATETIME_FORMAT": "%d %b %Y",
}

if not DEBUG:
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",)
    }

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(' ')

if not DEBUG:
    BASE_URL = "https://" + ALLOWED_HOSTS[0]
else:
    BASE_URL = "http://" + ALLOWED_HOSTS[1]

if not DEBUG:
    SECURE_HSTS_SECONDS = 3600
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = "SAMEORIGIN"  # if needed set to deny to avoid clickjacking protection
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_REFERRER_POLICY = "same-origin"

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'corsheaders',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'rest_framework_simplejwt',
    'users',
    'videos',
    'assessment',
    'feedback',
    "django_filters",
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.gitpod\.io$",
    ]

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOWED_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = (
        "http://localhost:8000",
        "http://localhost:3000",
    )

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(ROOT_DIR, "frontend", "build")
        ],
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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.environ.get("SQL_USER", "user"),
            "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
            "HOST": os.environ.get("SQL_HOST", "localhost"),
            "PORT": os.environ.get("SQL_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = (
    "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
)
STATIC_ROOT = os.path.join(ROOT_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(ROOT_DIR, "frontend", "build", "assets")]

WHITENOISE_ROOT = os.path.join(ROOT_DIR, "frontend", "build")

CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_NAME"),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),
    "API_SECRET": os.environ.get("CLOUDINARY_SECRET"),
}
MEDIA = '/media/'
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = "apikey"
    EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API")
    DEFAULT_FROM_EMAIL = os.environ.get("SENDGRID_FROM_EMAIL")
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=24),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_ON_GET = True
