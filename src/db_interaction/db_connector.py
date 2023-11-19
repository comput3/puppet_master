# db_connector.py

import cx_Oracle
import logging
from config import db_config  # Assuming database config is stored in a separate config file

class DBConnector:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(
                user=db_config['username'],
                password=db_config['password'],
                dsn=db_config['dsn']
            )
            logging.info("Database connection established.")
        except cx_Oracle.DatabaseError as e:
            logging.error(f"Database connection failed: {e}")
            raise

    def disconnect(self):
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")
