import sqlite3 

conn = sqlite3.connect("lections.sql")
#conn2 = sqlite3.connect("lections2.sql")
#conn3 = sqlite3.connect("lections3.sql")
cursor = conn.cursor()
#cursor2 = conn2.cursor()
#cursor3 = conn3.cursor()

query = "CREATE TABLE IF NOT EXISTS lections (numbers INT, title TEXT, author TEXT)"
cursor.execute(query)

info = [[1, "SQL beginner level", "Evgen"], [2, "SQL interm level", "Evgen"], [3, "SQL advanced level", "Evgen"]]
query = "INSERT INTO lections VALUES(?, ?, ?)"
#for i in info:
#    cursor.execute(query, i)
#    conn.commit()

query = "SELECT * FROM lections WHERE numbers > 1 AND title = 'SQL advanced level'"
for s in cursor.execute(query):
    print(s)

query = "DELETE  FROM lections WHERE numbers <= 1"
cursor.execute(query)
conn.commit()


cursor.close()
conn.close()