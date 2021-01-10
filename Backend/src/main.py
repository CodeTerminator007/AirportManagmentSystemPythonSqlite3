from tkinter import*
from tkinter import ttk
import os
import tkinter.messagebox as tkMessageBox
from database import *
from tkcalendar import DateEntry
        
class Authentication(Datbase):

    def __init__(self  ):
        pass


    def check_username_password(self,txt_user, txt_pass):
        username = txt_user.get()
        password = txt_pass.get()

        if username:
            if password:
                obj = Datbase() #creating the object of DATABASSE CLASS
                values = obj.Show_all_users_data() #calling ShowFunction FROM DATABASECLASS
                blackflag = False
                for value in values:
                    usern = value[3]
                    passw = value[5]
                    if usern == username and passw == password:
                        self.pk = value[0]
                        close()
                        obj = Home()                      
                        obj.view(self.pk)
                        blackflag = True
                    else:
                        blackflag = False
                if blackflag == False :
                    BothFlag = 3
                    return BothFlag
                else:
                    pass
            else:
                PasswordFlag = 2
                return PasswordFlag

        else:
            UsernameFlag = 1
            return UsernameFlag



# Login page root here
root=Tk()
root.title("Login System")
root.geometry("800x600+400+70")
root.resizable(False, False)

def close():
    root.destroy()


class Home(Authentication):
    def __init__(self):
        pass
    

    def view(self,pk):    
    
        obj = Datbase()

        value =  obj.show_specif_user_data(pk)

        root = Tk(className = "Airport Managment System")

        root.geometry("1500x1080+0+0")

        root.resizable(False, False)

        myLabel = Label(root, text = "Airport Managment System",
                        font = ("Arial",35,"bold"))

        myLabel.place(x = 375, y = 25)

        def closehome():
            result = tkMessageBox.askquestion('', 'Are you sure you want to quit', icon="question") 
            if result ==  "yes":
                root.destroy()

        for val in value:
            first = val[1]
            second = val[2]
        name = (f"User: {first} {second}")
        username = Label(root , text=name , font = ("Arial",10), bg = "grey78" )
        username.place(x=1300 , y=10)
        Flights_obj = Flights()
        #Buttons
        b1 = Button(root, text = "Flights", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white", command=Flights_obj.view)

        b1.place(x = 150, y = 130)
        Buy_Tickets_obj = Buy_Tickets()
        b2 = Button(root, text = "Buy Ticket", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white", command=Buy_Tickets_obj.buy )

        b2.place(x = 550, y = 130)
        Passangers_obj = Passangers()
        b3 = Button(root, text = "Passangers", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white" , command=Passangers_obj.view)

        b3.place(x = 950, y = 130)
        Addflightbj = ADD_FLIGHT()
        b4 = Button(root, text = "Add a Flight", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white" ,command=Addflightbj.view)

        b4.place(x = 150, y = 450)

        UpdateUser_obj = UpdateUser()
        b5 = Button(root, text = "User/Setting", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white",command=UpdateUser_obj.view)

        b5.place(x = 550, y = 450 )

        b6 = Button(root, text = "Logout", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white",command=closehome)

        b6.place(x = 950, y = 450)


        root.mainloop()

#Importing the Whole Flights Class Where You can Update Delete And view All Flights Data

from Flight import Flights

from Passanger import Passangers

from User import UpdateUser

from Buy import Buy_Tickets


from AddFlight import ADD_FLIGHT



class LoginWindow(Datbase):
    def __init__(self):
        pass

    def view(self):
        Frame_Login=Frame(root,bg="white")
        Frame_Login.place(relx=0.5,rely=0.5, anchor = CENTER ,  height=380,width=500)

        title=Label(Frame_Login,text="Login ",font=("Impact",35,"bold"),fg="black",bg="white")
        title.place(x=90,y=30)

        desc=Label(Frame_Login,text="Management Login Area",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        desc.place(x=90,y=100)

        lbl_user=Label(Frame_Login,text="User Name",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_user.place(x=90,y=140)
        
        txt_user=Entry(Frame_Login,font=("times new roman",15),bg="white")
        txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_Login,text="Password",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_pass.place(x=90,y=210)
        
        txt_pass=Entry(Frame_Login,font=("times new roman",15),bg="white")
        txt_pass.config(show="*")
        txt_pass.place(x=90,y=240,width=350,height=35)



        #creating object of Authentication Class
        obj = Authentication() 
        def run():
            returned = obj.check_username_password(txt_user,txt_pass)
            if returned == 1:
                tkMessageBox.showwarning('', 'Username Field is empty', icon="warning") 
            if returned ==2:
                tkMessageBox.showwarning('', 'Password Field is empty', icon="warning") 
            if returned == 3 :
                tkMessageBox.showwarning('', 'Wrong Username or Password', icon="warning")         

        login_btn=Button(Frame_Login,text="Login",bg="white",fg="black",font=("times new roman",15),command=run)
        login_btn.place(x=90,y=320,width=180,height=40)
        root.mainloop()



# running here
runloginwindowobj = LoginWindow()
runloginwindowobj.view()

