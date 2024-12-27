# verumveil/main.py
import logging

from utils.config import setup_logging
from cli import main as cli_main

# Logger
setup_logging()

logger = logging.getLogger(__name__)
logger.info("Application started.")

if __name__ == '__main__':
   cli_main.main()