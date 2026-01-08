import logging
from .config import settings


def get_logger(name: str):
level = logging.DEBUG if settings.DEBUG else logging.INFO
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s', level=level)
return logging.getLogger(name)


logger = get_logger('rag')
