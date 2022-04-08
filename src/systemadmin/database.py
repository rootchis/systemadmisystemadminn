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
        print(f"create DB{dbfile}")
        table = table
        conn = None
        try:
            conn = sqlite3.connect(dbfile)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

dbz = Databaz()
dbz.createdb("../../tests/resources/db/pythonsqlite.db", "")

