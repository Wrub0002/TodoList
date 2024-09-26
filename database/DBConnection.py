# DBConnection.py

import sqlite3

class DBConnection:
    _instance = None

    def __new__(cls, db_file):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(db_file)
        return cls._instance

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            DBConnection._instance = None
