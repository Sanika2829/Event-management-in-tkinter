import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as ms
import sqlite3

root=Tk()
root.title("Event")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))


userid = tk.IntVar()
name = tk.StringVar()
address = tk.StringVar()
contact = tk.IntVar()
email = tk.StringVar()
password = tk.StringVar()
password1 = tk.StringVar()

def password_check(password):
    SpecialSym=['$','@','#','%']
    val=True 
    
    if len(password)<6:
        print('Length should be at least 6')
        val=False
        
    if len(password)>20:
        print('Length should be not be greater than 8')
        val=False
    
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False 
        
    if not any(char.isupper() for char in password):
        print('Password should have at least upper case')
        val=False 
        
    if not any(char.islower() for char in password):
        print('Password should have at least lower case')
        val=False
        
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbol $@#')
        val=False
        
    if val :
        return val

def insert():
    Uid=userid.get()
    nm=name.get()
    call=contact.get()
    mail=email.get()
    pass1=password.get()
    pass2=password1.get()
    print(Uid)
    print(nm)
    print(call)
    print(mail)
    print(pass1)
    print(pass2)
    
    cnt=0
    no=call
    while(no!=0):
        rem=no%10
        no=no//10
        cnt+=1
    print(cnt)
    
    with sqlite3.connect('customer.db') as db:
        c=db.cursor()
        
    find_user=('SELECT * FROM customer WHERE Userid=?')
    c.execute(find_user,[(userid.get())])
    
    import re
    regex="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    if (re.search(regex, mail)):
        a=True
    else:
        a=False
        
    if c.fetchall():
        print("Try different userid")
        ms.showerror('Error!','Userid already exists try different one')
        
    elif nm=="" or nm.isdigit():
        ms.showerror('Error!','Enter valid username')
        
    elif call=="" or cnt!=10:
        ms.showerror("Error!","Enter valid contact number")
        
    elif mail=="" or a==False :
        ms.showerror('Error!','Enter valid mail')
    
    elif pass1=="":
        ms.showerror('Error!','Enter valid password')
    
    elif pass2=="" or pass1!=pass2:
        ms.showerror("Error","Password not match try again ")
        
    else:
         print("Insert into database")
         conn=sqlite3.connect('customer.db')
         with conn:
             cursor=conn.cursor()
             cursor.execute('INSERT INTO customer(Userid,Name,Contact,Mail,Password) VALUES(?,?,?,?,?)',
                            (Uid,nm,call,mail,pass1))
             conn.commit()
             conn.close()
             ms.showinfo('Success!','account created successfully')
             root.destroy()
              
             from subprocess import call
             call(['python','login.py'])   
    

image1=Image.open("f2.png")
image1=image1.resize((w,h),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=800,y=0)

# def login():
#     from subprocess import call
#     call(["python","login.py"])
#     root.destroy()
    
# frame = tk.LabelFrame(root, text="", width=400, height=579, bd=4, font=('times', 14, ' bold '),bg="white")
# frame.grid(row=0, column=0, sticky='nw')
# frame.place(x=170, y=88)


lbl = tk.Label(root, text="Registeration Form", font=('times', 20,' bold '), height=1, width=18,bg="steel blue",fg="white")
lbl.place(x=200, y=35)

l2 = tk.Label(root, text="User ID:", width=8, font=("Times new roman", 15, "bold"), bg="white",bd=5, fg="black")
l2.place(x=150, y=120)
t1 = tk.Entry(root, textvar=userid, width=26, font=('', 15),bd=4, bg="Hotpink3")
t1.place(x=290, y=120)

l3 = tk.Label(root, text="Name:", width=8, font=("Times new roman", 15, "bold"), bg="white",bd=5, fg="black")
l3.place(x=150, y=200)
t2 = tk.Entry(root, textvar=name, width=26, font=('', 15),bd=4, bg="Hotpink3")
t2.place(x=290, y=200)

l4 = tk.Label(root, text="Address:", width=8, font=("Times new roman", 15, "bold"), bg="white",bd=5, fg="black")
l4.place(x=150, y=270)
t3 = tk.Entry(root, textvar=address, width=29, font=('times', 15),bd=4, bg="Hotpink3")
t3.place(x=290, y=270)


l4 = tk.Label(root, text="Contact:", width=8, font=("Times new roman", 15, "bold"), bg="white",bd=5, fg="black")
l4.place(x=150, y=340)
t3 = tk.Entry(root, textvar=contact, width=29, font=('times', 15),bd=4, bg="Hotpink3")
t3.place(x=290, y=340)

l5 = tk.Label(root, text="Email:", width=8, font=("Times new roman", 15, "bold"), bg="white",bd=5, fg="black")
l5.place(x=150, y=410)
t5 = tk.Entry(root, textvar=email, width=29, font=('times', 15),bd=4, bg="Hotpink3")
t5.place(x=290, y=410)

l6 = tk.Label(root, text="Password:", width=8, font=("Times new roman", 15, "bold"), bg="white",bd=5, fg="black")
l6.place(x=150, y=480)
t6 = tk.Entry(root, textvar=password, width=29,show="*", font=('times', 15),bd=4, bg="Hotpink3")
t6.place(x=290, y=480)

l7 = tk.Label(root, text="Confirm Pass:", width=9, font=("Times new roman", 15, "bold"), bg="white",bd=5, fg="black")
l7.place(x=150, y=550)
t7 = tk.Entry(root, textvar=password1, width=29,show="*", font=('times', 15),bd=4, bg="Hotpink3")
t7.place(x=290, y=550)

button=Button(root,text="Submit",bg="green",width=10,height=1,fg="white",font=("times",20,"bold"),command=insert)
button.place(x=150,y=650)

button=Button(root,text="Cancel",bg="red4",width=10,height=1,fg="white",font=("times",20,"bold"))
button.place(x=400,y=650)


root.mainloop()