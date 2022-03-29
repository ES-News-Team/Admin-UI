import logging

__log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

logging.basicConfig(
    filemode='w',
    level=logging.DEBUG,
    format=__log_format
)

logger = logging.getLogger(__name__)