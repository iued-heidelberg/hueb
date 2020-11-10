import atexit
import os

import beeline


def honeycomb_config():
    if not os.getenv("ENV") == "GITHUB_WORKFLOW":
        if not os.getenv("HUEB_ENV") == "development":
            beeline.init(
                writekey=os.getenv("HUEB_HONEYCOMB_API_KEY"),
                dataset="hueb_" + os.getenv("HUEB_ENV"),
                service_name="django",
                debug=False,
                presend_hook=presend,
            )
            atexit.register(beeline.close)


def presend(fields):
    pass
