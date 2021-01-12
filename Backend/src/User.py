import datetime
import tkinter.messagebox as tkMessageBox
from tkinter import *
from tkinter import ttk

from database import Database


class UpdateUser:
    def __init__(self,pk):
        self.pk = pk
    def view(self):            
        root = Tk(className="Airport Managment System : User Information")
        root.geometry("1200x800+150+0")

        Myframe = Frame(root,bg = "white")
        Myframe.place(relx=0.5,rely=0.5, anchor = CENTER ,height=650,width=800)

        obj = Database()
        Logged_user_data = obj.show_specif_user_data(self.pk)
        for x in Logged_user_data:
            first_name = x[1]
            last_name = x[2]
            username = x[3]
            email = x[4]
            password = x[5]
            lastupdated = x[7]


        Label1 = Label(Myframe, text = "User Information",font = ("Times New Roman",35,"bold"),bg = "white")
        Label1.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        lbl_first_Name = Label(Myframe, text = "First Name",font = ("Times New Roman",16), bg = "white")
        lbl_first_Name.place(x=90,y=140 )
        txt_first_name = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        txt_first_name.place(x=90,y=170,width=250,height=30)
        txt_first_name.insert(0,first_name)

        lbl_Last_Name = Label(Myframe, text = "Last Name",font = ("Times New Roman",16), bg = "white")
        lbl_Last_Name.place(x=450,y=140)
        txt_Last_Name = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        txt_Last_Name.place(x=450,y=170,width=250,height=30)
        txt_Last_Name.insert(0,last_name)

        lbl_Email = Label(Myframe, text = "Email",font = ("Times New Roman",16), bg = "white")
        lbl_Email.place(x=90,y=220)
        txt_Email = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        txt_Email.place(x=90,y=250,width=250,height=30)
        txt_Email.insert(0,email)

        lbl_UserName = Label(Myframe, text = "UserName",font = ("Times New Roman",16), bg = "white")
        lbl_UserName.place(x=450,y=220)
        txt_UserName = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        txt_UserName.place(x=450,y=250,width=250,height=30)
        txt_UserName.insert(0,username)

        lbl_Current_password = Label(Myframe, text = "Current Password",font = ("Times New Roman",16), bg = "white")
        lbl_Current_password.place(x=90,y=300)
        txt_Current_password = Entry(Myframe, show="*" ,font = ("Times New Roman",14),width = 20)
        txt_Current_password.place(x=90,y=330,width=250,height=30)

        lbl_New_password = Label(Myframe, text = "New Password",font = ("Times New Roman",16), bg = "white")
        lbl_New_password.place(x=450,y=300)
        txt_New_password = Entry(Myframe, show="*" ,font = ("Times New Roman",14),width = 20)
        txt_New_password.place(x=450,y=330,width=250,height=30)

        lbl_Confirm_password = Label(Myframe, text = "Confirm New Password",font = ("Times New Roman",16), bg = "white")
        lbl_Confirm_password.place(x=90,y=380)
        txt_Confirm_password = Entry(Myframe, show="*" ,font = ("Times New Roman",14),width = 20)
        txt_Confirm_password.place(x=90,y=410,width=250,height=30)                  

        lbl_last_updated_at = Label(Myframe, text = "Last Updated at",font = ("Times New Roman",16), bg = "white")
        lbl_last_updated_at.place(x=450,y=380)
        txt_last_updated_at = Entry(Myframe,font = ("Times New Roman",14),width = 20)
        txt_last_updated_at.place(x=450,y=410,width=250,height=30)
        txt_last_updated_at.insert(0,lastupdated)        
        
        def closeUser():
            root.destroy()

        def UpdateUser():

            #Getting values from Inputs
            first_name_entered = txt_first_name.get()
            last_name_entered = txt_Last_Name.get()
            email_entered = txt_Email.get()
            Username_entered = txt_UserName.get()
            current_password_entered = txt_Current_password.get()
            New_password_entered = txt_New_password.get()
            Confirm_password_entered = txt_Confirm_password.get()
            
            #Declaring Boolean Values
            blackflag1 = False
            blackflag2 = False
            blackflag3 = False
            blackflag4 = False
            currentpasswordempty = False
            notchangepassword1 = False
            notchangepassword2 = False
            usernamenotchanged = False
            usernamechanged = False

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
                    if Username_entered == user[3] and self.pk != user[0]:
                        tkMessageBox.showwarning('', 'Username is Takken!', icon="warning" ,parent=Myframe) 
                    if Username_entered == user[3] and self.pk ==user[0]:
                        usernamenotchanged = True
                    if Username_entered != user[3] and self.pk !=user[0]:
                        usernamechanged = True
                        


            if current_password_entered =='':
                dot=Label(Myframe,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=330)
                currentpasswordempty = True                 
            else:
                pass

            if New_password_entered == '':
                notchangepassword1 = True
            else:
                notchangepassword1 = False
            if Confirm_password_entered == '':
                notchangepassword2 = True
            else:
                notchangepassword2 = False
           

            if blackflag1 == True or blackflag2 ==True or blackflag3 == True or blackflag4 ==True or currentpasswordempty ==True :
                tkMessageBox.showwarning('', 'Please Fill the * fields ', icon="warning" ,parent=Myframe)                               
            else:
                #if new password is Not entered
                if current_password_entered == password and notchangepassword1 == True and notchangepassword2 ==True:
                    if usernamenotchanged ==True or usernamechanged ==True:
                        obj.update_user_with_pk(self.pk,first_name_entered,last_name_entered,Username_entered,update_email,current_password_entered)
                        closeUser()
                    else:
                        pass
                else:
                    pass
                #if new password is entered
                if current_password_entered == password and  notchangepassword1 ==False and notchangepassword2 ==False:
                    if usernamenotchanged ==True or usernamechanged ==True:
                        if New_password_entered == Confirm_password_entered:
                            obj.update_user_with_pk(self.pk,first_name_entered,last_name_entered,Username_entered,update_email,New_password_entered)
                            closeUser()
                        else:
                            tkMessageBox.showwarning('', 'New Password Does Not Match!', icon="warning" ,parent=Myframe)               
                    else:
                        pass                

                            


        btn_Update_User = Button(Myframe, text = "Update",font=("times new roman",15),bg = "white",command=UpdateUser)
        btn_Update_User.place(x=90,y=540,width=180,height=40)      


        root.mainloop()
