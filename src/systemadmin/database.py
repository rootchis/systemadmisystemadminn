import sqlite3
from sqlite3 import Error

import pandas as pd


class Database:

    def __init__(self):
        print(f"Runnning Database with sqlite: {sqlite3.version}")

    #        self.database = database
    #        self.table = table
    #        self.connection = sqlite3.connect(database)

    def select(self, table):
        self.connection.execute(f"SELECT * FROM {table}")

    def insert(self, dictionnaire):
        if dictionnaire is dict:
            pass

    def createdb(self, dbfile, table):
        table = table
        """ create a database connection to a SQLite database """

        conn = None
        try:
            conn = sqlite3.connect(dbfile)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


db = Database()
db.createdb("../../tests/resources/db/pythonsqlite.db", "")
