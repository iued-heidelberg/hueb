import os

import beeline


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
