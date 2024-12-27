# verumveil/utils/config.py
import logging
import os

def setup_logging(default_level=logging.INFO):
    log_level = os.getenv("LOG_LEVEL", default_level)
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )