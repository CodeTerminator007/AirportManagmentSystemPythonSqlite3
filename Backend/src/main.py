from tkinter import*
from tkinter import ttk
import os
import tkinter.messagebox as tkMessageBox
from database import *
from tkcalendar import  DateEntry
        
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

        b3 = Button(root, text = "Passangers", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white")

        b3.place(x = 950, y = 130)

        b4 = Button(root, text = "Add a Flight", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white")

        b4.place(x = 150, y = 450)

        UpdateUser_obj = UpdateUser()
        b5 = Button(root, text = "User/Setting", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white",command=UpdateUser_obj.view)

        b5.place(x = 550, y = 450 )

        b6 = Button(root, text = "Logout", padx = 90, pady = 90,
                    font = ("Arial",15), bg = "white",command=closehome)

        b6.place(x = 950, y = 450)


        root.mainloop()

 
class Flights:
    def __init__(self):
        pass

    def view(self):
        root=Tk()
        root.geometry("1400x800+100+1")
        root.title("Flights record")
        
    
        Frame_Records=Frame(root,bg="white")
        Frame_Records.place(relx=0.5,rely=0.5,anchor=CENTER,height=750,width=1300)
        
        title=Label(Frame_Records,text="Flights record",font=("Impact",35,"bold"),fg="black",bg="white")
        title.place(x=400,y=50)
        
        txt_search=Entry(Frame_Records,font=("times new roman",15),bg="white")
        txt_search.place(x=750,y=130,width=250,height=25)
        
        
         
        tree_frame = Frame(Frame_Records)
        tree_frame.place(relx=0.5,rely=0.6,anchor=CENTER,height=550,width=1100)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        #Tree view Here
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        my_tree.place(relx=0.5,rely=0.5,anchor=CENTER,height=450,width=1000)

        tree_scroll.config(command=my_tree.yview)

        # Tree View Columns
        my_tree['columns'] = ("ID", "Company", "Flight Number","Seats",
        "Avaliable Seats" ,"From","To","Departure Time","Arrival Time")

        def selectItemUpdate():
            curItem = my_tree.focus()
            dict_val = my_tree.item(curItem)  #Getting Seleted item
            tt = {'text': '', 'image': '', 'values': '', 'open': 0, 'tags': ''}
            if dict_val == tt:
                tkMessageBox.showinfo('','Please Select a Flight you want to Update . ',icon='warning',parent=Frame_Records)
            else:
                root = Tk(className="User Information")
                root.geometry("800x700+400+0")
                def closethis():
                    root.destroy()
                Myframe = Frame(root,bg = "white")
                Myframe.place(relx = 0.5, rely = 0.5, anchor = CENTER,
                            height = 600,width = 650)

                Label1 = Label(Myframe, text = "Flight Information",
                            font = ("Times New Roman",35,"bold"),
                            bg = "white")
                

                data = dict_val['values']

                #specifieng the values from list
                theid = data[0]
                companyname = data[1]
                flightnumber = data[2]
                totalseats = data[3]
                avalseats = data[4]
                fromwhere = data[5]
                towhere = data[6]
                departuretime = data[7]
                arrivaltime = data[8]

                def save():    
                    result = tkMessageBox.askquestion('', 'Are you sure you want change', icon='question',parent=Myframe)                
                    if result == 'yes':
                        obj = Datbase()
                        obj.update_flight_with_pk(theid,company_name_enter.get(),flight_number_enter.get(),
                        total_seats_enter.get(),avaliable_seats_enter.get(),from_where_enter.get(),
                        to_where_enter.get(),departure_time_enter.get(),arrival_time_enter.get())
                        closethis()
                Label1.place(relx = 0.5, rely = 0.1, anchor = CENTER)

                company_name = Label(Myframe, text = "Company Name",
                            font = ("Times New Roman",16), bg = "white")

                company_name.place(x = 70, y = 120 )

                company_name_enter = Entry(Myframe,font = ("Times New Roman",14),
                            width = 20)
                company_name_enter.place(x = 70, y = 160)
                company_name_enter.insert(0,companyname)


                flight_number = Label(Myframe, text = "Flight Number",
                            font = ("Times New Roman",16), bg = "white")

                flight_number.place(x = 370, y = 120 )

                flight_number_enter = Entry(Myframe,font = ("Times New Roman",14),
                            width = 20)

                flight_number_enter.place(x = 370, y = 160)
                flight_number_enter.insert(0,flightnumber )           

                total_seats = Label(Myframe, text = "Total Seats",
                            font = ("Times New Roman",16), bg = "white")

                total_seats.place(x = 70, y = 220 )

                total_seats_enter = Entry(Myframe,font = ("Times New Roman",14),
                            width = 20)

                total_seats_enter.place(x = 70, y = 260)
                total_seats_enter.insert(0,totalseats)

                avaliable_seats = Label(Myframe, text = "Available Seats",
                            font = ("Times New Roman",16), bg = "white")

                avaliable_seats.place(x = 370, y = 220 )

                avaliable_seats_enter = Entry(Myframe,font = ("Times New Roman",14),
                            width = 20)

                avaliable_seats_enter.place(x = 370, y = 260)
                avaliable_seats_enter.insert(0,avalseats)

                from_where = Label(Myframe, text = "From",
                            font = ("Times New Roman",16), bg = "white")

                from_where.place(x = 70, y = 320 )

                from_where_enter = Entry(Myframe ,font = ("Times New Roman",14),
                            width = 20)

                from_where_enter.place(x = 70, y = 360)
                from_where_enter.insert(0,fromwhere)

                to_where = Label(Myframe, text = "To",
                            font = ("Times New Roman",16), bg = "white")

                to_where.place(x = 370, y = 320 )

                to_where_enter = Entry(Myframe,font = ("Times New Roman",14),
                            width = 20)

                to_where_enter.place(x = 370, y = 360)
                to_where_enter.insert(0,towhere)


                departure_time = Label(Myframe, text = "Departure Time",
                            font = ("Times New Roman",16), bg = "white")

                departure_time.place(x = 70, y = 420 )

                departure_time_enter = Entry(Myframe ,font = ("Times New Roman",14),
                            width = 20)

                departure_time_enter.place(x = 70, y = 460)
                departure_time_enter.insert(0,departuretime)


                arrival_time = Label(Myframe, text = "Arrival Time",
                            font = ("Times New Roman",16), bg = "white")

                arrival_time.place(x = 370, y = 420 )

                arrival_time_enter = Entry(Myframe,font = ("Times New Roman",14),
                            width = 20)

                arrival_time_enter.place(x = 370, y = 460)            
                arrival_time_enter.insert(0,arrivaltime)


                Button1 = Button(Myframe, text = "Change",font = ("Times New Roman",15),bg = "white" , command=save)
                Button1.place(relx = 0.2, rely = 0.9)


                root.mainloop()
        def selectItemdelete():
            curItem = my_tree.focus()
            dict_val = my_tree.item(curItem)
            tt = {'text': '', 'image': '', 'values': '', 'open': 0, 'tags': ''}
            if dict_val == tt:
                tkMessageBox.showinfo('','Please Select a Flight you want to delete . ',icon='warning',parent=Frame_Records)
            else:
                data = dict_val['values']
                result = tkMessageBox.askquestion('','Are you sure you want to delete the selected flight data remember it cannot be recovered.',icon='question',parent=Frame_Records)
                if result == 'yes':            
                    theid = data[0]                
                    obj.Delete_flight_pk(theid)





        #Update and Delete buttons
        updateflight_btn=Button(Frame_Records,text="Update",bg="white",fg="black",font=("times new roman",15),command=selectItemUpdate)
        updateflight_btn.place(x=130,y=130,width=100,height=25) 

        delete_flight=Button(Frame_Records,text="Delete",bg="white",fg="black",font=("times new roman",15),command=selectItemdelete)
        delete_flight.place(x=250,y=130,width=100,height=25)

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID",  width=20)
        my_tree.column("Company",  width=100)
        my_tree.column("Flight Number",  width=100)
        my_tree.column("Seats",  width=100)
        my_tree.column("Avaliable Seats", width=100)
        my_tree.column("From", width=100)
        my_tree.column("To",  width=100)
        my_tree.column("Departure Time",  width=100)
        my_tree.column("Arrival Time",  width=100)

        # Create Headings 
        my_tree.heading("#0", text="" )
        my_tree.heading("ID", text="ID" )
        my_tree.heading("Company", text="Company"  )
        my_tree.heading("Flight Number", text="Flight Number"  )
        my_tree.heading("Seats", text="Seats")
        my_tree.heading("Avaliable Seats", text="Avaliable Seats")
        my_tree.heading("From", text="From")
        my_tree.heading("To", text="To" )
        my_tree.heading("Departure Time", text="Departure Time")
        my_tree.heading("Arrival Time", text="Arrival Time")

        obj = Datbase()
        data = obj.Show_all_flights_data() #all flights data list here
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="lightblue")

        global count
        count=0

        for record in data:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,record[3], record[4], record[5],record[6] , record[7] ,record[8] , record[9] ), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,  record[3],record[4] , record[5] ,record[6] , record[7],record[8] , record[9] ),tags=('oddrow',))

            count += 1
        def search_function():
            if  txt_search.get() =='':
                tkMessageBox.showinfo('','Please enter the location of flight you want to search.',icon='warning',parent=Frame_Records)
            else:
                data_entered = txt_search.get()
                result_list = obj.show_specif_flight_data(data_entered)
                for i in my_tree.get_children():
                    my_tree.delete(i)
                for record in result_list:
                    count=0
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,record[3], record[4], record[5],record[6] , record[7] ,record[8] , record[9] ), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,  record[3],record[4] , record[5] ,record[6] , record[7],record[8] , record[9] ),tags=('oddrow',))

                
        search_btn=Button(Frame_Records,text="Search",bg="white",fg="black",font=("times new roman",15),command=search_function)
        search_btn.place(x=1010,y=130,width=100,height=25)        
           
        root.mainloop()



class UpdateUser:
    def __init__(self):
        pass
    def view(self):            
        root = Tk(className="User Information")
        root.geometry("800x700")

        Myframe = Frame(root,bg = "white")
        Myframe.place(relx = 0.5, rely = 0.5, anchor = CENTER,
                    height = 600,width = 650)

        Label1 = Label(Myframe, text = "User Information",
                    font = ("Times New Roman",35,"bold"),
                    bg = "white")

        Label1.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        first_Name = Label(Myframe, text = "First Name",
                    font = ("Times New Roman",16), bg = "white")

        first_Name.place(x = 70, y = 120 )

        Entry1 = Entry(Myframe,font = ("Times New Roman",14),
                    width = 20)

        Entry1.place(x = 70, y = 160)


        Last_Name = Label(Myframe, text = "Last Name",
                    font = ("Times New Roman",16), bg = "white")

        Last_Name.place(x = 370, y = 120 )

        Entry2 = Entry(Myframe,font = ("Times New Roman",14),
                    width = 20)

        Entry2.place(x = 370, y = 160)

        Email = Label(Myframe, text = "Email",
                    font = ("Times New Roman",16), bg = "white")

        Email.place(x = 70, y = 220 )

        Entry3 = Entry(Myframe,font = ("Times New Roman",14),
                    width = 20)

        Entry3.place(x = 70, y = 260)

        Cnfrm_Email = Label(Myframe, text = "Confirm Email",
                    font = ("Times New Roman",16), bg = "white")

        Cnfrm_Email.place(x = 370, y = 220 )

        Entry3 = Entry(Myframe,font = ("Times New Roman",14),
                    width = 20)

        Entry3.place(x = 370, y = 260)

        Password = Label(Myframe, text = "Password",
                    font = ("Times New Roman",16), bg = "white")

        Password.place(x = 70, y = 320 )

        Entry4 = Entry(Myframe, show="*" ,font = ("Times New Roman",14),
                    width = 20)

        Entry4.place(x = 70, y = 360)

        Cnfrm_pass = Label(Myframe, text = "Confirm Password",
                    font = ("Times New Roman",16), bg = "white")

        Cnfrm_pass.place(x = 370, y = 320 )

        Entry5 = Entry(Myframe, show="*" ,font = ("Times New Roman",14),
                    width = 20)

        Entry5.place(x = 370, y = 360)

        Button1 = Button(Myframe, text = "Update",
                        font = ("Times New Roman",20),
                    bg = "white")
        Button1.place(relx = 0.5, rely = 0.8, anchor = CENTER)


        root.mainloop()


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

