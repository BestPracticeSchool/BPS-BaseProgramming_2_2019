import sqlite3
import create_db

class Schooler(User):
    pass 

class User:
    def __init__(self, email:str, name : str, surname : str , age : int):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email 

    def insert(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        query = "INSERT INTO users VALUES(?,?,?,?)"
        cur.execute(query, (self.name, self.surname, self.age, self.email))

        conn.commit()
        conn.close()

u = User("John", "Travolta", 65, "@@#")
u.insert()


#CRUD -- CREATE READ UPDATE DELETE
