import sqlite3

db=sqlite3.connect('feedback.db')
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS feedback"
               "(userid NUMBER,feed TEXT)")

db.commit()
db.close()


