import logging.handlers
import logging
from datetime import datetime

logging.getLogger('').setLevel(logging.NOTSET)
logfile_name = datetime.now().strftime('log_%Y%m%d_%H%M.log')
rotatingHandler = logging.handlers.RotatingFileHandler(
    filename=logfile_name, maxBytes=1024 * 1024 * 10, backupCount=5, encoding='utf-8')
rotatingHandler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotatingHandler.setFormatter(formatter)
logging.getLogger('').addHandler(rotatingHandler)
log = logging.getLogger("content_managment " + __name__)

# Пососи мою писю