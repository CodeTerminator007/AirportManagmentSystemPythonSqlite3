import time
import tkinter.messagebox as tkMessageBox
from tkinter import *

from tkcalendar import DateEntry

from database import *


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

        root = Tk()
        root.title("Airport Managment System : Home")
        root.geometry("1500x1080+10+0")
        root.resizable(False, False)
        #Clock code Here
        def clock_update():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            am_pm = time.strftime("%p")
            clock_label.config(text=f'{hour} : {minute} : {second} {am_pm }')
            clock_label.after(1000,clock_update)

        clock_label = Label(root,text='',fg='black',font = ("times new roman",16,'bold'))
        clock_label.place(x=1350,y=5)   


        HomeFrame = Frame(root)
        HomeFrame.place(relx=0.01,rely=0.05,width=1470 ,height=1000)

        myLabel = Label(root, text = "Airport Managment System",font = ("Impact",35),fg='black')
        myLabel.place(x = 450, y = 0)
        clock_update()


        color2= 'grey50'
        #total values of flights passangerd code here
        total_passangers_frame = Frame(HomeFrame,bg=color2,highlightbackground="white",highlightthickness=2)
        total_passangers_frame.place(x=180,y=40,width=250,height=140)
        total_passanger_label = Label(total_passangers_frame,bg=color2,fg='white',text='Total Passangers',font=("times new roman",16,'bold'))
        total_passanger_label.place(relx=0.2,y=10)
        total_passanger_num = Label(total_passangers_frame,bg=color2,fg='white',text='',font=("times new roman",20))
        total_passanger_num.place(relx=0.4,y=60)


        total_flights_arrived_frame = Frame(HomeFrame,bg=color2,highlightbackground="white",highlightthickness=2)
        total_flights_arrived_frame.place(x=580,y=40,width=250,height=140)
        total_flights_arrived_label = Label(total_flights_arrived_frame,bg=color2,fg='white',text='Flights Arrived',font=("times new roman",16,'bold'))
        total_flights_arrived_label.place(relx=0.2,y=10)
        total_flights_arrived_num = Label(total_flights_arrived_frame,bg=color2,fg='white',text='',font=("times new roman",20))
        total_flights_arrived_num.place(relx=0.4,y=60) 


        Departed_flights_num_frame = Frame(HomeFrame,bg=color2,highlightbackground="white",highlightthickness=2)
        Departed_flights_num_frame.place(x=980,y=40,width=250,height=140)
        Departed_flights_label = Label(Departed_flights_num_frame,bg=color2,fg='white',text='Departed Flights',font=("times new roman",16,'bold'))
        Departed_flights_label.place(relx=0.2,y=10)
        Departed_flights_num = Label(Departed_flights_num_frame,bg=color2,fg='white',text='',font=("times new roman",20))
        Departed_flights_num.place(relx=0.4,y=60)                   

        def uptime():
            all_passangers = len(obj.Show_all_passangers_data())
            all_flights = obj.Show_all_flights_data()
            arrived_number = 0
            departed_number = 0
            for flight in all_flights:
                arrivedflight_time = flight[8]
                Arrival_time_obj = datetime.datetime.strptime(arrivedflight_time, '%Y-%m-%d %H:%M:%S')
                departedflight_time = flight[7]
                Departed_time_obj = datetime.datetime.strptime(departedflight_time, '%Y-%m-%d %H:%M:%S')

                if datetime.datetime.now() >= Arrival_time_obj and datetime.datetime.now() <= Departed_time_obj:
                    arrived_number = arrived_number + 1
                if  datetime.datetime.now() > Departed_time_obj:
                    departed_number = departed_number + 1

            total_passanger_num.config(text=all_passangers)
            total_flights_arrived_num.config(text=arrived_number)
            Departed_flights_num.config(text=departed_number)
            Departed_flights_num.after(1000,uptime)

        uptime() #calling the functions

        #Objects Of Different Classes
        Flights_obj = Flights()
        Buy_Tickets_obj = Buy_Tickets()
        Passangers_obj = Passangers()
        Addflightbj = ADD_FLIGHT()
        UpdateUser_obj = UpdateUser(pk)


        b1 = Button(HomeFrame, text = "Flights", padx = 90, pady = 90,font = ("Arial",20), fg='black', bg='white',command=Flights_obj.view)
        b1.place(x = 150, y = 210,width=300,height =200)

        b2 = Button(HomeFrame, text = "Buy Ticket", padx = 90, pady = 90,font = ("Arial",20),fg='black', bg='white',command=Buy_Tickets_obj.buy )
        b2.place(x = 550, y = 210,width=300,height =200)

        b3 = Button(HomeFrame, text = "Passangers", padx = 90, pady = 90,font = ("Arial",20),fg='black',bg='white', command=Passangers_obj.view)
        b3.place(x = 950, y = 210,width=300,height =200)

        b4 = Button(HomeFrame, text = "Add a Flight", padx = 90, pady = 90,font = ("Arial",20),fg='black',bg='white',command=Addflightbj.view)
        b4.place(x = 150, y = 480 ,width=300,height =200)

        b5 = Button(HomeFrame, text = "User", padx = 90, pady = 90,font = ("Arial",20),fg='black',bg='white',command=UpdateUser_obj.view)
        b5.place(x = 550, y = 480 ,width=300,height =200)

        def closehome():
            result = tkMessageBox.askquestion('', 'Are you sure you want to quit', icon="question") 
            if result ==  "yes":
                root.destroy()
            else:
                pass

        b6 = Button(HomeFrame, text = "Logout", padx = 90, pady = 90,font = ("Arial",20),fg='black',bg='white',command=closehome)
        b6.place(x = 950, y = 480,width=300,height =200)


        root.mainloop()

#Importing Classes From Files

from AddFlight import ADD_FLIGHT
from Buy import Buy_Tickets
from Flight import Flights
from Passanger import Passangers
from User import UpdateUser


class LoginWindow(Database):
    def __init__(self):
        pass

    def view(self):
        root=Tk()
        root.title("Airport Managment System : Login")
        root.geometry("800x600+400+70")
        root.configure(background='gray8')

        root.resizable(False, False)


        Frame_Login=Frame(root,bg="gray8")
        Frame_Login.place(relx=0.5,rely=0.5, anchor = CENTER ,  height=380,width=500)

        title=Label(Frame_Login,text="Login ",font=("Impact",35,"bold"),fg="White",bg="gray8")
        title.place(relx=0.4,y=30)

        desc=Label(Frame_Login,text="Management Login Area",font=("Goudy old style",15,"bold"),fg="white",bg="gray8")
        desc.place(x=90,y=100)

        lbl_user=Label(Frame_Login,text="User Name",font=("Goudy old style",15,"bold"),fg="white",bg="gray8")
        lbl_user.place(x=90,y=140)
        
        txt_user=Entry(Frame_Login,font=("times new roman",15),bg="gray9",fg='white')
        txt_user.place(x=90,y=170,width=350,height=35)
        txt_user.config(insertbackground='white')

        lbl_pass=Label(Frame_Login,text="Password",font=("Goudy old style",15,"bold"),fg="white",bg="gray8")
        lbl_pass.place(x=90,y=210)
        
        txt_pass=Entry(Frame_Login,font=("times new roman",15),bg="gray9",fg='white')
        txt_pass.config(show="*")   
        txt_pass.place(x=90,y=240,width=350,height=35)
        txt_pass.config(insertbackground='white')

        #creating object of Authentication Class
        obj = Authentication() 
        def run():
            returned = obj.check_username_password(txt_user,txt_pass)
            if returned == 'username':
                tkMessageBox.showwarning('', 'Empty Field', icon="warning") 
            if returned =='password':
                tkMessageBox.showwarning('', 'Password Field is empty', icon="warning") 
            if returned == 'both' :
                tkMessageBox.showwarning('', 'Wrong Username or Password', icon="warning")
            if returned != 'username' and returned != 'password' and returned != 'both':
                objhome = Home()
                root.destroy()
                objhome.view(returned)

        login_btn=Button(Frame_Login,text="Login",bg="gray9",fg="white",font=("times new roman",15),command=run)
        login_btn.place(x=90,y=320,width=160,height=40)
        def adduser():            
            from AddUser import ADDUSER
            user_obj = ADDUSER()
            user_obj.view()            
        adduser_btn = Button(Frame_Login,text="Add User",bg="gray9",fg="white",font=("times new roman",15),command=adduser)
        adduser_btn.place(x=280,y=320,width=160,height=40)
        root.mainloop()

runloginwindowobj = LoginWindow()
runloginwindowobj.view()

