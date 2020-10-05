import os

import beeline


def honeycomb_config():
    if not os.getenv("ENV") == "GITHUB_WORKFLOW":
        return beeline.init(
            writekey=os.getenv("HUEB_HONEYCOMB_API_KEY"),
            dataset="hueb_" + os.getenv("HUEB_ENV"),
            service_name="hueb",
            debug=False,
            presend_hook=presend,
        )


def presend(fields):
    pass
