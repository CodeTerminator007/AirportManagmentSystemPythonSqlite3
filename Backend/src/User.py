from tkinter import*
from tkinter import ttk
import tkinter.messagebox as tkMessageBox

class UpdateUser:
    def __init__(self):
        pass
    def view(self):            
        root = Tk(className="Airport Managment System : User Information")
        root.geometry("800x700")

        Myframe = Frame(root,bg = "white")
        Myframe.place(relx = 0.5, rely = 0.5, anchor = CENTER,height = 600,width = 650)

        Label1 = Label(Myframe, text = "User Information",font = ("Times New Roman",35,"bold"),bg = "white")
        Label1.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        first_Name = Label(Myframe, text = "First Name",font = ("Times New Roman",16), bg = "white")
        first_Name.place(x = 70, y = 120 )
        Entry1 = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        Entry1.place(x = 70, y = 160)


        Last_Name = Label(Myframe, text = "Last Name",font = ("Times New Roman",16), bg = "white")
        Last_Name.place(x = 370, y = 120 )
        Entry2 = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        Entry2.place(x = 370, y = 160)

        Email = Label(Myframe, text = "Email",font = ("Times New Roman",16), bg = "white")
        Email.place(x = 70, y = 220 )
        Entry3 = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        Entry3.place(x = 70, y = 260)

        Cnfrm_Email = Label(Myframe, text = "Confirm Email",font = ("Times New Roman",16), bg = "white")
        Cnfrm_Email.place(x = 370, y = 220 )
        Entry3 = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        Entry3.place(x = 370, y = 260)

        Password = Label(Myframe, text = "Password",font = ("Times New Roman",16), bg = "white")
        Password.place(x = 70, y = 320 )
        Entry4 = Entry(Myframe, show="*" ,font = ("Times New Roman",14),width = 20)
        Entry4.place(x = 70, y = 360)

        Cnfrm_pass = Label(Myframe, text = "Confirm Password",font = ("Times New Roman",16), bg = "white")
        Cnfrm_pass.place(x = 370, y = 320 )
        Entry5 = Entry(Myframe, show="*" ,font = ("Times New Roman",14),width = 20)
        Entry5.place(x = 370, y = 360)

        Button1 = Button(Myframe, text = "Update",font = ("Times New Roman",20),bg = "white")
        Button1.place(relx = 0.5, rely = 0.8, anchor = CENTER)


        root.mainloop()
