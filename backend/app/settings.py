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

import os
import dj_database_url

if os.path.exists(find_dotenv()):
    load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "users/templates")

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
    # Instruct web browser to remember the HSTS policy for 3600 secs (1
    # hour), in this time if the user tries to access the website using HTTP
    # the browser automatically converts it to HTTPS - mitigates the risk of
    # man-in-the-middle attacks that can intercept and modify HTTP requests.
    SECURE_HSTS_SECONDS = 3600
    # Prevents browsers from interpreting files as a different MIME type
    # than declared by the server
    SECURE_CONTENT_TYPE_NOSNIFF = True
    # Prevents Cross-Site-Scripting (XSS) protections, by using sanitising
    # and filtering user input
    SECURE_BROWSER_XSS_FILTER = True
    # Redirects HTTP to HTTPs. All communication between client and server
    # is encrypted and secure
    SECURE_SSL_REDIRECT = True
    # Only send cookie over HTTPS connection
    SESSION_COOKIE_SECURE = True
    # Only send Cross-Site-Request-Forgery (CSRF) over HTTPS connection
    CSRF_COOKIE_SECURE = True
    # Prevents the site from being embedded in any frame, protect from
    # clickjacking attacks
    X_FRAME_OPTIONS = "DENY"
    # Ensures the HSTS policy is applied to the main domain and its
    # subdomains - enhancing security
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # Allows the website to be included in the HSTS Preload list. Ensures
    # that the browser is always accessible via HTTPS (from first visit)
    SECURE_HSTS_PRELOAD = True
    # Allows the app to detect the original protocol used by the client
    # before it reached the proxy (useful when Django app is deployed behind
    # reverse proxy (e.g. Nginx / Apache)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    # `same-origin` ensures the referrer information is only sent when
    # navigating to the same origin, helping protect user privacy
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

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # React's default port
# ]

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOWED_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = (
        "http://localhost:8000",
    )

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
            os.path.join(BASE_DIR, 'staticfiles', 'build')
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
STATIC_ROOT = BASE_DIR / 'staticfiles'
WHITENOISE_ROOT = BASE_DIR / 'staticfiles' / 'build'

CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_NAME"),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),
    "API_SECRET": os.environ.get("CLOUDINARY_SECRET"),
}
MEDIA = '/media/'
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# A warning but causes issues when implemented https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STORAGES
# STORAGES = {
#     "default": {
#         "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "cloudinary_storage.storage.StaticHashedCloudinaryStorage",
#     },
# }

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = 'users.Profile'

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
