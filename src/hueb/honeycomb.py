import atexit
import os

import beeline


def honeycomb_config():
    if os.getenv("HONEYCOMB_API_KEY") is not None:
        beeline.init(
            writekey=os.getenv("HONEYCOMB_API_KEY"),
            dataset="hueb_" + os.getenv("ENV"),
            service_name="django",
            debug=False,
            presend_hook=presend,
        )
        atexit.register(beeline.close)


def presend(fields):
    pass
