import datetime
import tkinter.messagebox as tkMessageBox
from tkinter import *
from tkinter import ttk
import re
from database import Database


class ADDUSER:
    def __init__(self):
        pass
    def view(self):            
            root = Tk(className="Airport Managment System : Add User")
            root.geometry("1100x700+150+0")

            Myframe = Frame(root,bg = "white")
            Myframe.place(relx=0.5,rely=0.5, anchor = CENTER ,height=550,width=800)


            Label1 = Label(Myframe, text = "Add User",font = ("Times New Roman",35,"bold"),bg = "white")
            Label1.place(relx = 0.5, rely = 0.1, anchor = CENTER)

            lbl_first_Name = Label(Myframe, text = "First Name",font = ("Times New Roman",16), bg = "white")
            lbl_first_Name.place(x=90,y=140 )
            txt_first_name = Entry(Myframe,font = ("Times New Roman",14),width = 20)
            txt_first_name.place(x=90,y=170,width=250,height=30)

            lbl_Last_Name = Label(Myframe, text = "Last Name",font = ("Times New Roman",16), bg = "white")
            lbl_Last_Name.place(x=450,y=140)
            txt_Last_Name = Entry(Myframe,font = ("Times New Roman",14),width = 20)
            txt_Last_Name.place(x=450,y=170,width=250,height=30)

            lbl_Email = Label(Myframe, text = "Email",font = ("Times New Roman",16), bg = "white")
            lbl_Email.place(x=90,y=220)
            txt_Email = Entry(Myframe,font = ("Times New Roman",14),width = 20)
            txt_Email.place(x=90,y=250,width=250,height=30)

            lbl_UserName = Label(Myframe, text = "UserName",font = ("Times New Roman",16), bg = "white")
            lbl_UserName.place(x=450,y=220)
            txt_UserName = Entry(Myframe,font = ("Times New Roman",14),width = 20)
            txt_UserName.place(x=450,y=250,width=250,height=30)

            lbl_password = Label(Myframe, text = "Password",font = ("Times New Roman",16), bg = "white")
            lbl_password.place(x=90,y=300)
            txt_password = Entry(Myframe, show="*" ,font = ("Times New Roman",14),width = 20)
            txt_password.place(x=90,y=330,width=250,height=30)

            lbl_Confirm_password = Label(Myframe, text = "Confirm Password",font = ("Times New Roman",16), bg = "white")
            lbl_Confirm_password.place(x=450,y=300)
            txt_Confirm_password = Entry(Myframe, show="*" ,font = ("Times New Roman",14),width = 20)
            txt_Confirm_password.place(x=450,y=330,width=250,height=30)

            def closeUser():
                root.destroy()
                
            def Submit():
                obj = Database()
                #Getting values from Inputs
                first_name_entered = txt_first_name.get()
                last_name_entered = txt_Last_Name.get()
                email_entered = txt_Email.get()
                Username_entered = txt_UserName.get()
                password = txt_password.get()
                confirm_password = txt_Confirm_password.get()
                created_at = datetime.datetime.now()

                #Declaring Boolean Values
                blackflag1 = False
                blackflag2 = False
                blackflag3 = False
                blackflag4 = False    
                usernametaken = False  
                passwordempty = False
                confirmpassword = False

                if first_name_entered =='':
                    dot=Label(Myframe,text="*",font=("Goudy old style",20,"bold"),
                    fg="red",bg="white")
                    dot.place(x=60,y=170)
                    blackflag1 = True                
                else:
                    pass
                if last_name_entered =='':
                    dot=Label(Myframe,text="*",font=("Goudy old style",20,"bold"),
                    fg="red",bg="white")
                    dot.place(x=420,y=170)
                    blackflag2 = True
                else:
                    pass
                regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
                if re.search(regex,email_entered):
                    update_email = email_entered
                else:
                    dot=Label(Myframe,text="*",font=("Goudy old style",20,"bold"),
                    fg="red",bg="white")
                    dot.place(x=60,y=250)
                    blackflag3 = True
                if Username_entered =='':
                    dot=Label(Myframe,text="*",font=("Goudy old style",20,"bold"),
                    fg="red",bg="white")
                    dot.place(x=420,y=250)
                    blackflag4 = True
                else:
                    users = obj.Show_all_users_data()
                    for user in users:
                        if Username_entered == user[3]:
                            usernametaken =True

                if password =='':
                    dot=Label(Myframe,text="*",font=("Goudy old style",20,"bold"),
                    fg="red",bg="white")
                    dot.place(x=60,y=330)
                    passwordempty = True                 
                else:
                    pass
                if confirm_password == '':
                    dot=Label(Myframe,text="*",font=("Goudy old style",20,"bold"),
                    fg="red",bg="white")
                    dot.place(x=420,y=330)
                    confirmpassword = True  
                else:
                    pass
                if usernametaken==False:
                    if blackflag1 == True or blackflag2 ==True or blackflag3 == True or blackflag4 ==True or passwordempty ==True or confirmpassword ==True :
                        tkMessageBox.showwarning('', 'Please Fill the * fields ', icon="warning" ,parent=Myframe)                               
                    else:
                        if password == confirm_password and usernametaken== False:
                            obj.Insert_data_users(first_name_entered,last_name_entered,Username_entered,update_email,password,created_at)
                            closeUser()
                        else:
                            tkMessageBox.showwarning('', 'Password Does Not Match!', icon="warning" ,parent=Myframe)               
                else:
                    tkMessageBox.showwarning('', 'Username is Taken', icon="warning" ,parent=Myframe)               

            
            btn_Add_User = Button(Myframe, text = "Submit",font=("times new roman",15),bg = "white",command=Submit)
            btn_Add_User.place(x=90,y=400,width=180,height=40)     

            root.mainloop()
