import sqlite3


def execute_sql(query):
    conn = sqlite3.connect("data/company.db")
    cursor = conn.cursor()

    try:
        cursor.execute(query)

        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        rows = cursor.fetchall()

        conn.close()

        return columns, rows, None

    except Exception as e:
        conn.close()
        return None, None, str(e)