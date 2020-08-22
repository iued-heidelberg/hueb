"""
Django settings for hueb project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hueb.settings")


ENV = os.environ.get("ENV", None)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if os.getenv("HUEB_STATIC_DIR") is not None:
    STATIC_ROOT = os.getenv("HUEB_STATIC_DIR")
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("HUEB_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("HUEB_DEBUG") == "TRUE"

ALLOWED_HOSTS = [os.getenv("HUEB_ALLOWED_HOSTS")]


INSTALLED_APPS = [
    "hueb.apps.hueb20",
    "hueb.apps.hueb_legacy_latein",
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
]

MIDDLEWARE = [
    "beeline.middleware.django.HoneyMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "hueb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hueb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if ENV == "GITHUB_WORKFLOW":
    DEBUG = True
    SECRET_KEY = "TESTING_KEY"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("HUEB_DATABASE_NAME"),
            "USER": os.getenv("HUEB_DATABASE_USER"),
            "PASSWORD": os.getenv("HUEB_DATABASE_PASSWORD"),
            "HOST": os.getenv("HUEB_DATABASE_HOST"),
            "PORT": os.getenv("HUEB_DATABASE_PORT"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


INTERNAL_IPS = ["127.0.0.1"]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"


if os.getenv("HUEB_SENTRY_INACTIVE") is None:
    sentry_sdk.init(
        dsn=os.getenv("HUEB_SENTRY_API_KEY"),
        integrations=[DjangoIntegration()],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        environment=os.getenv("HUEB_ENV"),
    )
