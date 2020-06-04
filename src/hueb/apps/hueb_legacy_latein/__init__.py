import os

import beeline
from django.apps import AppConfig


def honeycomb_config():
    return beeline.init(
        writekey=os.getenv("HUEB_HONEYCOMB_API_KEY"),
        dataset="hueb_legacy",
        service_name="hueb",
        debug=False,
        presend_hook=presend,
    )


def presend(fields):
    fields["env"] = os.getenv("HUEB_ENV")


class HuebLegacyLateinConfig(AppConfig):
    name = "hueb.apps.hueb_legacy_latein"
    verbose_name = "Hueb Legacy Latein"

    def ready(self):
        # this call is for the local development setup
        # you have to call it in gunicorn.conf.py as well
        honeycomb_config()


default_app_config = "hueb.apps.hueb_legacy_latein.HuebLegacyLateinConfig"
