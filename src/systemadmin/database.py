import sqlite3
from sqlite3 import Error

#import pandas as pd



class Databaz:
    def __init__(self):
        print(f"Runnning Database with sqlite: {sqlite3.version}")

    def select(self, table):
        self.connection.execute(f"SELECT * FROM {table}")

    def insert(self, dictionnaire):
        if dictionnaire is dict:
            pass

    def createdb(self, dbfile, table):
        table = table
        conn = None
        try:
            conn = sqlite3.connect(dbfile)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    dbz = Databaz()

    dbz.createdb("../../tests/resources/db/pythonsqlite.db", "")

