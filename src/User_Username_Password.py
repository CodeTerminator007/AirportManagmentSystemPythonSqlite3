import datetime
import tkinter.messagebox as tkMessageBox
from tkinter import *
from tkinter import ttk

from database import Database


class USER_EMAIL:
    def __init__(self):
        self.email = ''
        self.password  = ''       
    def view(self):            
            root = Tk(className="Airport Managment System : User ")
            root.geometry("700x600+400+70")
            root.resizable(False,False)
            Myframe = Frame(root,bg = "white")
            Myframe.place(relx=0.5,rely=0.5, anchor = CENTER ,height=450,width=500)


            Label1 = Label(Myframe, text = "Airport Managment System",font = ("Times New Roman",25,"bold"),bg = "white")
            Label1.place(relx = 0.5, rely = 0.1, anchor = CENTER)

            lbl_username = Label(Myframe, text = "Email",font = ("Times New Roman",16), bg = "white")
            lbl_username.place(x=90,y=140 )
            txt_username = Entry(Myframe,font = ("Times New Roman",14),width = 20)
            txt_username.place(x=90,y=170,width=250,height=30)
            lbl_password = Label(Myframe, text = "Password",font = ("Times New Roman",16), bg = "white")
            lbl_password.place(x=90,y=200)
            txt_password = Entry(Myframe, show="*" ,font = ("Times New Roman",14),width = 20)
            txt_password.place(x=90,y=240,width=250,height=30)
            
            def close():
                root.destroy()
            def submit():
                self.email =  txt_username.get()
                self.password =  txt_password.get()
                file = open("usernamepassword.py","w") 
                file.write(f"EMAIL_ADDRESS = '{self.email}'\n") 
                file.write(f"EMAIL_PASSWORD = '{self.password}'") 
                file.close() 
                close()                                            
            label2 = Label(Myframe,text='Looks Like Software needs a Email and Password for The Managment System \nto send Mails Enter its Email And Password Here' , fg="red",bg="white",font=("times new roman",11))
            label2.place(x=10,y=80)
            labell = Label(Myframe,text='Note: Once Data Given this window will not appear Ever ' , fg="red",bg="white",font=("times new roman",11))
            labell.place(x=90,y=400)
            btn_Add_User = Button(Myframe, text = "Save",font=("times new roman",15),bg = "white",command=submit)
            btn_Add_User.place(x=90,y=290,width=180,height=40)     

            root.mainloop()
