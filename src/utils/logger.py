import logging
import sys


def setup_logging() -> None:
    """Set up logging configuration."""
    format_string = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"

    logging.basicConfig(
        level=logging.INFO,
        format=format_string,
        datefmt="%H:%M:%S",
        stream=sys.stdout,
    )
