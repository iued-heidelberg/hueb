from django.apps import AppConfig
from hueb.honeycomb import honeycomb_config


class HuebLegacyLateinConfig(AppConfig):
    name = "hueb.apps.hueb_legacy_latein"
    verbose_name = "Hueb Legacy Latein"

    def ready(self):
        # this call is for the local development setup
        # you have to call it in gunicorn.conf.py as well
        honeycomb_config()


default_app_config = "hueb.apps.hueb_legacy_latein.HuebLegacyLateinConfig"
