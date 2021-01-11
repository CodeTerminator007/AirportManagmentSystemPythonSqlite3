from tkinter import*
import tkinter.messagebox as tkMessageBox
from database import *
from tkcalendar import DateEntry
        
class Authentication(Database):

    def __init__(self  ):
        pass

    def check_username_password(self,txt_user, txt_pass):
        username = txt_user.get()
        password = txt_pass.get()

        if username:
            if password:
                obj = Database() 
                values = obj.Show_all_users_data()
                blackflag = False
                for value in values:
                    usern = value[3]
                    passw = value[5]
                    if usern == username and passw == password:
                        logged_user_pk = value[0]
                        return logged_user_pk
                    else:
                        pass
                if blackflag == False :
                    BothFlag = 'both'
                    return BothFlag
            else:
                PasswordFlag = 'password'
                return PasswordFlag

        else:
            UsernameFlag = 'username'
            return UsernameFlag

class Home(Authentication):
    def __init__(self):
        pass
    

    def view(self,pk):    
        obj = Database()

        value =  obj.show_specif_user_data(pk)
        root = Tk()
        root.title("Airport Managment System : Home")
        root.geometry("1500x1080+10+0")

        root.resizable(False, False)
        HomeFrame = Frame(root)
        HomeFrame.place(relx=0.01,rely=0.05,width=1400 ,height=900)

        myLabel = Label(HomeFrame, text = "Airport Managment System",font = ("Arial",35,"bold"))
        myLabel.place(x = 375, y = 25)

        #logged Username 
        for val in value:
            first_name = val[1]
            second_name = val[2]
        name = (f"User: {first_name} {second_name}")
        username = Label(HomeFrame , text=name , font = ("Arial",10) )
        username.place(x=1200 , y=10)

        #Objects Of Different Classes
        Flights_obj = Flights()
        Buy_Tickets_obj = Buy_Tickets()
        Passangers_obj = Passangers()
        Addflightbj = ADD_FLIGHT()
        UpdateUser_obj = UpdateUser()


        b1 = Button(HomeFrame, text = "Flights", padx = 90, pady = 90,font = ("Arial",15), bg = "white", command=Flights_obj.view)
        b1.place(x = 150, y = 130,width=300,height =200)

        b2 = Button(HomeFrame, text = "Buy Ticket", padx = 90, pady = 90,font = ("Arial",15), bg = "white", command=Buy_Tickets_obj.buy )
        b2.place(x = 550, y = 130,width=300,height =200)

        b3 = Button(HomeFrame, text = "Passangers", padx = 90, pady = 90,font = ("Arial",15), bg = "white" , command=Passangers_obj.view)
        b3.place(x = 950, y = 130,width=300,height =200)

        b4 = Button(HomeFrame, text = "Add a Flight", padx = 90, pady = 90,font = ("Arial",15), bg = "white" ,command=Addflightbj.view)
        b4.place(x = 150, y = 450 ,width=300,height =200)

        b5 = Button(HomeFrame, text = "User", padx = 90, pady = 90,font = ("Arial",15), bg = "white",command=UpdateUser_obj.view)
        b5.place(x = 550, y = 450 ,width=300,height =200)

        def closehome():
            result = tkMessageBox.askquestion('', 'Are you sure you want to quit', icon="question") 
            if result ==  "yes":
                root.destroy()
            else:
                pass

        b6 = Button(HomeFrame, text = "Logout", padx = 90, pady = 90,font = ("Arial",15), bg = "white",command=closehome)
        b6.place(x = 950, y = 450,width=300,height =200)


        root.mainloop()

#Importing Classes From Files

from Flight import Flights
from Passanger import Passangers
from User import UpdateUser
from Buy import Buy_Tickets
from AddFlight import ADD_FLIGHT

class LoginWindow(Database):
    def __init__(self):
        pass

    def view(self):
        root=Tk()
        root.title("Airport Managment System : Login")
        root.geometry("800x600+400+70")
        root.resizable(False, False)


        Frame_Login=Frame(root,bg="white")
        Frame_Login.place(relx=0.5,rely=0.5, anchor = CENTER ,  height=380,width=500)

        title=Label(Frame_Login,text="Login ",font=("Impact",35,"bold"),fg="black",bg="white")
        title.place(relx=0.4,y=30)

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
            if returned == 'username':
                tkMessageBox.showwarning('', 'Username Field is empty', icon="warning") 
            if returned =='password':
                tkMessageBox.showwarning('', 'Password Field is empty', icon="warning") 
            if returned == 'both' :
                tkMessageBox.showwarning('', 'Wrong Username or Password', icon="warning")
            if returned != 'username' and returned != 'password' and returned != 'both':
                objhome = Home()
                root.destroy()
                objhome.view(returned)

        login_btn=Button(Frame_Login,text="Login",bg="white",fg="black",font=("times new roman",15),command=run)
        login_btn.place(x=90,y=320,width=180,height=40)
        root.mainloop()

runloginwindowobj = LoginWindow()
runloginwindowobj.view()

