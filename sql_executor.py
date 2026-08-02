import sqlite3
import pandas as pd

def execute_sql(query):
    try:
        conn = sqlite3.connect("data/company.db")
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        return str(e)
