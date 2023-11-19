# db_operations.py

import logging
from db_connector import DBConnector

class DBOperations:
    def __init__(self):
        self.connector = DBConnector()

    def execute_query(self, query, parameters=None):
        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, parameters or {})
            rowcount = cursor.rowcount
            self.connector.connection.commit()
            cursor.close()
            logging.info(f"Query executed successfully: {cursor.rowcount} rows affected.")
            return rowcount
        except cx_Oracle.DatabaseError as e:
            logging.error(f"Error executing query: {e}")
            raise
        finally:
            self.connector.disconnect()
