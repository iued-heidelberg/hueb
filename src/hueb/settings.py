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
from django.utils.translation import gettext_lazy as _

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hueb.settings")

LOGIN_REDIRECT_URL = "/admin"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "simple_history",
    "hueb.apps.hueb20",
    "hueb.apps.hueb_legacy_latein",
    "hueb.apps.hueb_legacy_lidos",
    "hueb.apps.hueb_legacy",
    "hueb.apps.user_history",
    "hueb.apps.publications",
    "django_extensions",
    # translations",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "import_export",
    "debug_toolbar",
    "rosetta",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "beeline.middleware.django.HoneyMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
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
                "hueb.apps.hueb20.context_processors.menu",
                "hueb.apps.hueb20.context_processors.overlay",
                "django.template.context_processors.i18n",
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


WSGI_APPLICATION = "hueb.wsgi.application"

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = "de"

# LANGUAGE_CODE = "de"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, "hueb/apps/hueb20/locale"),)
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
gettext = lambda s: s
LANGUAGES = (
    ("de", _("German")),
    ("en", _("English")),
)
MODELTRANSLATION_LANGUAGES = ("de", "en")

IS_MONOLINGUAL = False

# TRANSLATABLE_MODEL_MODULES = ["hueb.apps.hueb20.models.language"]

# MODELTRANSLATION_AUTO_POPULATE = True
# MODELTRANSLATION_DEBUG = False
# MODELTRANSLATION_ENABLE_FALLBACKS = True
# MODELTRANSLATION_FALLBACK_LANGUAGES =('de', 'en')
# MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'de'

# MODELTRANSLATION_TRANSLATION_FILES = (
#    "hueb.src.hueb.apps.hueb20.translation",
# )
INTERNAL_IPS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
ENV = os.environ.get("ENV", None)

if ENV == "GITHUB_WORKFLOW":
    DEBUG = False
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
    # SECURITY WARNING: keep the secret key used in production secret!

    DEBUG = os.getenv("DEBUG") == "True"
    print(DEBUG)
    SECRET_KEY = os.environ["SECRET_KEY"]
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        },
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


try:
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
except AttributeError:
    ALLOWED_HOSTS = "127.0.0.1"


if os.getenv("ENV") == "development":
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                # exact format is not important, this is the minimum information
                "format": "%(levelname)s %(asctime)s %(name)-12s  %(message)s",
            },
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "console"},
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }


if os.getenv("SENTRY_API_KEY") not in [None, "", " "]:

    sentry_sdk.init(
        dsn=os.getenv("SENTRY_API_KEY"),
        integrations=[DjangoIntegration()],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        environment=os.getenv("ENV"),
        release="hueb20@" + os.getenv("GIT_SHA", "NONE"),
    )


if os.getenv("STATIC_DIR") is not None:
    STATIC_ROOT = os.getenv("STATIC_DIR")
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
if os.getenv("MEDIA_DIR") is not None:
    MEDIA_ROOT = os.getenv("MEDIA_DIR")
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
