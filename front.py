#import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

root = Tk()
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.title("Event management system")

image1=Image.open("front.png")
image1=image1.resize((w,h),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

def Regis():
    from subprocess import call
    call(["python","custoregis.py"])
    root.destroy()
    

button=Button(root,text="Home",bg="white",width=10,height=1,fg="black",font=("times",20,"bold"))
button.place(x=50,y=50)

button=Button(root,text="Registration",command=Regis,bg="white",width=10,height=1,fg="black",font=("times",20,"bold"))
button.place(x=350,y=130)

button=Button(root,text="Login",bg="white",width=10,height=1,fg="black",font=("times",20,"bold"))
button.place(x=950,y=50)

button=Button(root,text="Feedback",bg="white",width=10,height=1,fg="black",font=("times",20,"bold"))
button.place(x=1250,y=130)

root.mainloop()