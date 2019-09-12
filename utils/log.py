import logging

from loguru import logger
from sentry_sdk.integrations.logging import EventHandler, BreadcrumbHandler


def init_log():
    logging.getLogger("chardet").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    class InterceptHandler(logging.Handler):
        def emit(self, record):
            # Retrieve context where the logging call occurred, this happens to be in the 6th frame upward
            logger_opt = logger.opt(depth=6, exception=record.exc_info)
            logger_opt.log(record.levelname, record.getMessage())

    logging.basicConfig(handlers=[InterceptHandler()], level=logging.DEBUG)

    logger.add(EventHandler(), format="{message}", level="ERROR")
    logger.add(BreadcrumbHandler(), format="{message}", level="ERROR")
