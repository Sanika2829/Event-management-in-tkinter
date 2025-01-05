import sqlite3

db=sqlite3.connect('event.db')
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS event"
               "(Userid Number,Name TEXT,Eventname TEXT, Time Number, Menu TEXT)")



db.commit()
db.close()


