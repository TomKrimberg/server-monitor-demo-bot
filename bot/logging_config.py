import logging
import sys
def setup_logging():
    logger = logging.getLogger("server_monitor")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger