# db_logger.py

import logging
import os

LOG_FILE = 'database_operations.log'

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename=os.path.join('logs', LOG_FILE),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
