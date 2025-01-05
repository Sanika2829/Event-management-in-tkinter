import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as ms
import sqlite3

root=Tk()
root.title("Event")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

Userid=tk.IntVar()
password=tk.StringVar()



image1=Image.open("login.jpg")
image1=image1.resize((1500,400),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)


user_icon=ImageTk.PhotoImage(file="U.jpeg")
pass_icon=ImageTk.PhotoImage(file="p.jpeg")

def login():
    un=Userid.get()
    pass1=password.get()
    
    with sqlite3.connect('customer.db') as db:
        c=db.cursor()
        
    find_user=('SELECT * FROM customer WHERE Userid=? and Password=?')
    c.execute(find_user,[(Userid.get()),(password.get())])
    result=c.fetchall()
    print(result)
    if result:
        msg='Login Successfully'
        print(msg)
        ms.showinfo('message','Login Sucessfully')
        from subprocess import call
        call(['python','AUD.py'])
        root.destroy()
        
    else:
        ms.showerror('Oops!','Username or Password Did Not Found/Match')
    



title=tk.Label(root,text="Login Here",font=("Times new roman",20),bd=5,bg="black",fg="white")
title.place(x=650,y=450,width=150)

login_frame=tk.Frame(root,bg="gray29")
login_frame.place(x=500,y=530)


lbluser=tk.Label(login_frame,text="Userid",image=user_icon,compound=LEFT,font=("Times new roman",20),
                 bg="white").grid(row=0,column=0,padx=20,pady=10)

txtuser=tk.Entry(login_frame,bd=5,textvariable=Userid,font=("times",15))
txtuser.grid(row=0,column=1,padx=20)

lbluser=tk.Label(login_frame,text="Password",image=pass_icon,compound=LEFT,font=("Times new roman",20),
                 bg="white" ).grid(row=1,column=0,padx=50,pady=10)

txtuser=tk.Entry(login_frame,bd=5,textvariable=password,font=("times",15))
txtuser.grid(row=1,column=1,padx=20)

btn=tk.Button(login_frame,text="Login",width=10,compound=LEFT,command=login,font=("Times new roman",20),
                 bg="green",fg="black",bd=3).grid(row=2,column=1,pady=10)

btn1=tk.Button(login_frame,text="Cancel",width=15,compound=LEFT,font=("Times new roman",20),
                 bg="skyblue",fg="black",bd=3).grid(row=2,column=0,pady=10)

root.mainloop()