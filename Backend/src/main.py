from tkinter import*
from tkinter import ttk
import smtplib
import os
from database import *
from tkcalendar import  DateEntry
import avaliable_destinations

class Authentication(Datbase):

    def __init__(self , txt_user, txt_pass):
        self.txt_user = txt_user
        self.txt_pass = txt_pass
    def check_username_password(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        if username:
            if password:
                obj = Datbase() #creating the object of DATABASSE CLASS
                values = obj.Show_all_users_data() #calling ShowFunction FROM DATABASECLASS
                for value in values:
                    usern = value[3]
                    passw = value[5]
                    if usern == username and passw == password:
                        self.pk = value[0]
                        close()
                        obj = Home()                      
                        obj.view(self.pk)
                        
                else:
                    pass
            else:
                print("Password is Missing")
        else:
            print("User Name is is Missing")





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
        for val in value:
            first = val[1]
            second = val[2]
        name = (f"User: {first} {second}")
        username = Label(root , text=name , font = ("Arial",10), bg = "grey78" )
        username.place(x=1300 , y=10)

        #Buttons
        flightobject = Flight_Schedule()
        b1 = Button(root, text = "Flight Schedule", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white", command=flightobject.view)

        b1.place(x = 150, y = 130)
        Buy_Tickets_obj = Buy_Tickets()
        b2 = Button(root, text = "Buy Ticket", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white", command=Buy_Tickets_obj.buy )

        b2.place(x = 550, y = 130)

        b3 = Button(root, text = "Passanger Record", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white")

        b3.place(x = 950, y = 130)

        b4 = Button(root, text = "Flight Records", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white")

        b4.place(x = 150, y = 450)

        b5 = Button(root, text = "Logout", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white")

        b5.place(x = 550, y = 450)

        b6 = Button(root, text = "Button 6", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white")

        b6.place(x = 950, y = 450)

        root.mainloop()

 
class Flight_Schedule:
    def __init__(self):
        pass
    def view(self):
        obj = Home()
        # all_flight_data =  obj.Show_all_flights_data()
        # print(all_flight_data)


# importing but_tickets Class
from Buy import Buy_Tickets


class Passanger_Record():
    #all passanger specific passanger
    def __init__(self):
        pass
    def view(self):
        pass
    def specific_passanger(self,passangerid):
        pass

class Add_Flight():
    def __init__(self):
        pass
    def view(self):
        pass
    def insert_flight(self,airlineName,flightnumber,noofseats,noofseatsavaliable,source,destination,timedatedeparture,timedatearrival):

        obj = Datbase()
        obj.Insert_data_flights(airlineName,flightnumber,noofseats,noofseatsavaliable,source,destination,timedatedeparture,timedatearrival , datetime.datetime.now())

        pass



class LoginWindow(Datbase):

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
    txt_pass.place(x=90,y=240,width=350,height=35)

    forget_btn=Button(Frame_Login,text="forget password",bg="white",fg="black",bd=0,font=("times new roman",12))
    forget_btn.place(x=90,y=280)

    #creating object of Authentication Class
    obj = Authentication(txt_user,txt_pass) 

    login_btn=Button(Frame_Login,text="Login",bg="white",fg="black",font=("times new roman",15),command=obj.check_username_password)
    login_btn.place(x=90,y=320,width=180,height=40)
    root.mainloop()



class Logout():
    pass



