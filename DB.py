import sqlite3

class DBHelper:
    def __init__(self):
        try:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("CREATE TABLE Games (BlueSide text,RedSide text,Score text)")
        except:
            pass
    def insertar(self,string):
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute(string)
        conn.commit()
        conn.close()
    def leer(self):
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Games")
        return c.fetchall()