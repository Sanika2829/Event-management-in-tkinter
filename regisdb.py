import sqlite3

db=sqlite3.connect('customer.db')
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS customer"
               "(Userid Number,Name TEXT,Address TEXT, Contact Number, Mail TEXT, Password TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS event"
               "(Userid Number,Name TEXT,Eventname TEXT, Time Number, Menu TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS feedback"
               "(Userid NUMBER,feed TEXT)")

db.commit()
db.close()