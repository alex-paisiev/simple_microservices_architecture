import logging
import sys

from app.core.config import settings

DETAILED_LOG_FORMAT = "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"
SIMPLE_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


def configure_logging() -> None:
    logger = logging.getLogger()  # Configure the root logger
    logger.setLevel(settings.LOG_LEVEL)

    # Create a StreamHandler for console output
    stream_handler = logging.StreamHandler(sys.stdout)
    log_formatter = logging.Formatter(SIMPLE_LOG_FORMAT)
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(stream_handler)
