from django.apps import AppConfig
from hueb.honeycomb import honeycomb_config


class Hueb20Config(AppConfig):
    name = "hueb.apps.hueb20"
    verbose_name = "Hueb20"

    def ready(self):
        # this call is for the local development setup
        # you have to call it in gunicorn.conf.py as well
        honeycomb_config()


default_app_config = "hueb.apps.hueb20.Hueb20Config"
