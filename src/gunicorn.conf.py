# conf.py
import logging
import os

from dotenv import load_dotenv
from hueb_legacy_latein.apps import honeycomb_config


def post_worker_init(worker):
    load_dotenv()
    logging.info(f"beeline initialization in process pid {os.getpid()}")
    honeycomb_config()
