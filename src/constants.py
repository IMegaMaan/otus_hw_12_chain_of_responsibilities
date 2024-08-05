import logging
from pathlib import Path

BASE_DIR: Path = Path(__file__).parent
LOGGING_FORMAT: str = "%(asctime)s [%(levelname)s] - (%(filename)s).%(funcName)s:%(lineno)d - %(message)s"
LOGGING_LEVEL: int = logging.DEBUG
