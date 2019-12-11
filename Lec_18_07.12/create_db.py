import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS users (name TEXT, surname TEXT, age INT, email TEXT)"
cur.execute(query)

conn.commit()
conn.close()