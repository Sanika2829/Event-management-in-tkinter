import sqlite3
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as ms
from tkinter import ttk



root = Tk()
root.title("Feedback")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

feedback=tk.StringVar()
#userid=tk.IntVar()


image1=Image.open("Feeds.jpg")
#image2=Image.open("img1.jpeg")
image1=image1.resize((w,h),Image.ANTIALIAS)
#image2=image2.resize((200,400),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

def Feedback():
    feed=feedback.get()
    
    
    Userid=('SELECT Userid FROM customer ')
    
    with sqlite3.connect('feedback.db') as db:
        c=db.cursor()
        result=c.fetchall()
        print(result)
        if result:
            msg='Thank You'
            print(msg)
            ms.showinfo('message','Thank You')
        
            
            
        else:
            print("Insert into database")
            conn=sqlite3.connect('feedback.db')
            with conn:
                cursor=conn.cursor()
                cursor.execute('INSERT INTO feedback (Userid,feed) VALUES(?,?) ',
                               (Userid,feed))
                conn.commit()
                conn.close()
                ms.showinfo('Success!','Thank you')
                root.destroy()

lbl = tk.Label(root, text="Feedback", font=('times', 20,' bold '), height=1, width=10,bg="white",fg="black")
lbl.place(x=300, y=150)

text = tk.Text(root,height=15,width=40)
text.place(x=250,y=250)

button=Button(root,text="Submit",bg="green",width=10,height=1,fg="white",font=("times",20,"bold"),command=Feedback)
button.place(x=300,y=550)


root.mainloop()