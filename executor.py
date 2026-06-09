import sqlite3
import pandas as pd

def execute(query):
    connection=sqlite3.connect("data.db")
    result=pd.read_sql_query(query,connection)

    connection.close()

    return result