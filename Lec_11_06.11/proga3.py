import sqlite3

conn = sqlite3.connect("my_data.sql")
cursor = conn.cursor()

name = "John"
surname = "Hasselhoff"
age = 9

query = "CREATE TABLE IF NOT EXISTS info (name TEXT, surname TEXT, age INT)"
cursor.execute(query)

query_insert = "INSERT INTO info VALUES(? ,?, ?)"

for i in range(1,10000):
    cursor.execute(query_insert, [name+str(i), surname+str(i), age + i])
    #if i % 5000 == 0:
     #   conn.commit()
conn.commit()


query_select = "SELECT name FROM info WHERE age > 45 AND age <= 70"
for i in cursor.execute(query_select):
    print(i)

cursor.close()
conn.close()