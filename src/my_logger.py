
import logging

import colorlog


def create_logger(name="app_logger"):
    # Create and configure logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    # Create a colored log format
    formatter = colorlog.ColoredFormatter(
        '%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(log_color)s%(message)s%(reset)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'blue',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )

    # Create console handler and set level to INFO
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    ch.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(ch)

    return logger

