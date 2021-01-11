from tkinter import*
from tkinter import ttk
import smtplib
import tkinter.messagebox as tkMessageBox
from database import *
from tkcalendar import DateEntry

class Passangers():
    def __init__(self):
        pass
    def view(self):
        root=Tk()
        root.geometry("1400x800+100+1")
        root.title("Airport Managment System : Passangers Records")
    
        Frame_Records=Frame(root,bg="white")
        Frame_Records.place(relx=0.5,rely=0.5,anchor=CENTER,height=750,width=1300)
        
        title=Label(Frame_Records,text="Passangers Record",font=("Impact",35,"bold"),fg="black",bg="white")
        title.place(x=400,y=50)
            
        #Tree View
        tree_frame = Frame(Frame_Records)
        tree_frame.place(relx=0.5,rely=0.6,anchor=CENTER,height=550,width=1100)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        my_tree.place(relx=0.5,rely=0.5,anchor=CENTER,height=450,width=1000)
        tree_scroll.config(command=my_tree.yview)


        # Tree View Columns
        my_tree['columns'] = ("ID","First Name","Last Name","Email","CNIC" ,"Date of Birth","Nationality","Flight","Last Modified at")


        #Creating Columns and Headings
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID", width=20)
        my_tree.column("First Name",  width=60)
        my_tree.column("Last Name",  width=60)
        my_tree.column("Email",  width=200)
        my_tree.column("CNIC", width=100)
        my_tree.column("Date of Birth", width=60)
        my_tree.column("Nationality", width=70)
        my_tree.column("Flight", width=60)
        my_tree.column("Last Modified at",  width=150)


        my_tree.heading("#0", text="" )
        my_tree.heading("ID", text="ID" )
        my_tree.heading("First Name", text="First Name"  )
        my_tree.heading("Last Name", text="Last Name"  )
        my_tree.heading("Email", text="Email")
        my_tree.heading("CNIC", text="Cnic")
        my_tree.heading("Date of Birth", text="Date of Birth")
        my_tree.heading("Nationality", text="Nationality")
        my_tree.heading("Flight", text="Flight")
        my_tree.heading("Last Modified at", text="Last Modified at" )


        obj = Database()
        data = obj.Show_all_passangers_data() 
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="lightblue")

        #Declaring Global Variable
        global count
        count=0
        #Inserting All Passanger Data
        for record in data:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,record[3], record[4], record[5],record[6] ,record[8] , record[11] ), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,  record[3],record[4] , record[5] ,record[6],record[8],record[11] ),tags=('oddrow',))
            count += 1


        #Searching Specific Passanger
        def search_function(event):

            #Declaring Global Variable 
            global count2
            global count3
            count3=0
            count2=0            
            if  txt_search.get() =='':
                val = obj.Show_all_passangers_data()

                for i in my_tree.get_children():
                    my_tree.delete(i)
                for record in val:                    
                    if count3 % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count3, text="", values=(record[0], record[1], record[2] ,record[3], record[4], record[5],record[6] , record[8] , record[11] ), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count3, text="", values=(record[0], record[1], record[2] ,  record[3],record[4] , record[5] ,record[6] ,record[8] , record[11] ),tags=('oddrow',))
                    count3 += 1                

            else:
                data_entered = txt_search.get()
                result_list = obj.search_specif_passanger_data(data_entered)

                for i in my_tree.get_children():
                    my_tree.delete(i)
                for record in result_list:                    
                    if count2 % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count2, text="", values=(record[0], record[1], record[2] ,record[3], record[4], record[5],record[6] , record[8] , record[11] ), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count2, text="", values=(record[0], record[1], record[2] ,  record[3],record[4] , record[5] ,record[6] ,record[8] , record[11] ),tags=('oddrow',))
                    count2 += 1


        def search_function_btn():

            #Declaring Global Variable 
            global count2
            global count3
            count3=0
            count2=0            
            if  txt_search.get() =='':
                val = obj.Show_all_passangers_data()

                for i in my_tree.get_children():
                    my_tree.delete(i)
                for record in val:                    
                    if count3 % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count3, text="", values=(record[0], record[1], record[2] ,record[3], record[4], record[5],record[6] , record[8] , record[11] ), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count3, text="", values=(record[0], record[1], record[2] ,  record[3],record[4] , record[5] ,record[6] ,record[8] , record[11] ),tags=('oddrow',))
                    count3 += 1                

            else:
                data_entered = txt_search.get()
                result_list = obj.search_specif_passanger_data(data_entered)

                for i in my_tree.get_children():
                    my_tree.delete(i)
                for record in result_list:                    
                    if count2 % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count2, text="", values=(record[0], record[1], record[2] ,record[3], record[4], record[5],record[6] , record[8] , record[11] ), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count2, text="", values=(record[0], record[1], record[2] ,  record[3],record[4] , record[5] ,record[6] ,record[8] , record[11] ),tags=('oddrow',))
                    count2 += 1

        
        def UpdatePassanger():
            curItem = my_tree.focus()
            dict_val = my_tree.item(curItem)  
            Default_val = {'text': '', 'image': '', 'values': '', 'open': 0, 'tags': ''}
            if dict_val == Default_val:
                tkMessageBox.showinfo('','Please Select a Passanger you want to Update . ',icon='warning',parent=Frame_Records)
            else:

                root = Tk(className="Passanger Information")
                root.geometry("800x700+400+0")

                def closeupdatewindow():
                    root.destroy()

                Myframe = Frame(root,bg = "white")
                Myframe.place(relx = 0.5, rely = 0.5, anchor = CENTER,height = 600,width = 650)

                Label1 = Label(Myframe, text = "Passanger Information",font = ("Times New Roman",35,"bold"),bg = "white")
                Label1.place(relx = 0.5, rely = 0.1, anchor = CENTER)
                
                data = dict_val['values']

                #specifieng the values from list
                theid = data[0]
                firstname = data[1]
                lastname = data[2]
                CNIC = data[4]
                Email = data[3]
                Date_of_birth = data[5]
                date_time_obj = datetime.datetime.strptime(Date_of_birth, '%Y-%m-%d')
                Nationality = data[6]
                flightnumber = data[7]
                flight_data = obj.show_specif_flight_data_with_flightnumber(flightnumber)
                flight_data_tuple = flight_data[0]

                first_name = Label(Myframe, text = "First Name",font = ("Times New Roman",16), bg = "white")
                first_name.place(x = 70, y = 120 )
                first_name_txt = Entry(Myframe,font = ("Times New Roman",14),width = 20)
                first_name_txt.place(x = 70, y = 160)
                first_name_txt.insert(0,firstname)


                last_name = Label(Myframe, text = "Last Name",font = ("Times New Roman",16), bg = "white")
                last_name.place(x = 370, y = 120 )
                last_name_txt = Entry(Myframe,font = ("Times New Roman",14),width = 20)
                last_name_txt.place(x = 370, y = 160)
                last_name_txt.insert(0,lastname )           


                email = Label(Myframe, text = "Email",font = ("Times New Roman",16), bg = "white" )
                email.place(x = 70, y = 220 )
                email_txt = Entry(Myframe,font = ("Times New Roman",14),width = 20)
                email_txt.place(x = 70, y = 260 , width = 250)
                email_txt.insert(0,Email)


                cnic = Label(Myframe, text = "CNIC",font = ("Times New Roman",16), bg = "white")
                cnic.place(x = 370, y = 220 )
                cnic_txt = Entry(Myframe,font = ("Times New Roman",14),width = 20)
                cnic_txt.place(x = 370, y = 260)
                cnic_txt.insert(0,CNIC)


                lbl_birth=Label(Myframe,text="Date of birth",font=("Goudy old style",15,"bold"),fg="black",bg="white")
                lbl_birth.place(x=70,y=320)
                cal = DateEntry(Myframe, width=12, background='white',foreground='black', borderwidth=2,year=date_time_obj.year, month=date_time_obj.month , day=date_time_obj.day)
                cal.place(x=70,y=355,width=250,height=30)


                nationality = Label(Myframe, text = "Nationality",font = ("Times New Roman",16), bg = "white")
                nationality.place(x = 370, y = 320 )
                nationality_txt = Entry(Myframe,font = ("Times New Roman",14),width = 20)
                nationality_txt.place(x = 370, y = 360)
                nationality_txt.insert(0,Nationality)
                

                flightnumbers = Label(Myframe, text = "Flight Number",font = ("Times New Roman",16), bg = "white")
                flightnumbers.place(x = 70, y = 420 )
                flightnumber_txt = Entry(Myframe,font = ("Times New Roman",14),width = 20)
                flightnumber_txt.place(x = 70, y = 460)
                flightnumber_txt.insert(0,flightnumber)


                flight_change = Label(Myframe, text = "Change Flight",font = ("Times New Roman",16), bg = "white")
                flight_change.place(x = 340, y = 420 )


                all_flights = obj.Show_all_flights_data()
                flight = []
                for x in all_flights:
                    id = x[0]
                    flight_name = x[2]
                    flight_num = x[1]
                    flight_time = x[7]
                    flight += [f"{id} {flight_name} {flight_num} leaves on {flight_time}"]  

                clickedhere = StringVar(Myframe)
                clickedhere.set(f"{flight_data_tuple[0] } {flight_data_tuple[1]} {flight_data_tuple[2]}")

                drop_down_flights= OptionMenu(Myframe, clickedhere,'Select Flight Here' ,*flight )      
                drop_down_flights.place(x=270,y=460,width=350,height=30)


                def send_mail(address,first_name,last_name,flight_name,flight_num , flight_time ):            
                    from usernamepassword import EMAIL_ADDRESS , EMAIL_PASSWORD

                    with smtplib.SMTP('smtp.gmail.com',587 ) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)

                        subject = 'Airport Ticket Change of Flight'
                        body = f'Hi {first_name} {last_name } This The Ticket has been Updated and the New Plane {flight_name} {flight_num} Will leave on {flight_time} Thanks for chosing us \n Regards Hussnain Ahmad '

                        msg = f"Subject:{subject}\n\n {body}"
                        smtp.sendmail(EMAIL_ADDRESS,address , msg)                

                def Update():
                    val = clickedhere.get()
                    if val=='Select Flight Here':
                        tkMessageBox.showinfo('','Please Select a Flight',icon='warning',parent=Myframe)
                        
                    else:
                        result = tkMessageBox.askquestion('', 'Are you sure you want change', icon='question',parent=Myframe)
                        flightid = int(val[0]) 
                        real_flight = obj.show_specif_flight_data_with_pk(flightid)                    
                        for s in real_flight:
                            flighname = s[1]
                            flighttime = s[6]
                            flight_number = s[2]
                            aval_seats = s[4]   
                        if aval_seats >= 1 :
                            if result == 'yes':
                                if flight_data_tuple[0] == flightid:
                                    obj.update_passanger_with_pk(theid,first_name_txt.get(),last_name_txt.get(),
                                    email_txt.get(),cnic_txt.get(),cal.get_date(),
                                    nationality_txt.get(),flightid,flight_number)
                                    closeupdatewindow() 
                                else:
                                    obj.update_passanger_with_pk(theid,first_name_txt.get(),last_name_txt.get(),
                                    email_txt.get(),cnic_txt.get(),cal.get_date(),
                                    nationality_txt.get(),flightid,flight_number)
                                    send_mail(email_txt.get(),first_name_txt.get(),last_name_txt.get(),flighname,flight_number,flighttime)
                                    closeupdatewindow()                                 

                        else: 
                                                       
                            tkMessageBox.showwarning('', 'No seats Avaliable ', icon="warning",parent=Myframe)  

                Button1 = Button(Myframe, text = "Update",font = ("Times New Roman",15),bg = "white" , command=Update)
                Button1.place(relx = 0.2, rely = 0.9)

                root.mainloop()

        def DeletePassanger():
            curItem = my_tree.focus()
            dict_val = my_tree.item(curItem)
            Default_val = {'text': '', 'image': '', 'values': '', 'open': 0, 'tags': ''}
            if dict_val == Default_val:
                tkMessageBox.showinfo('','Please Select a passanger you want to delete . ',icon='warning',parent=Frame_Records)
            else:
                data = dict_val['values']
                result = tkMessageBox.askquestion('','Are you sure you want to delete the selected passanger data remember it cannot be recovered.',icon='question',parent=Frame_Records)
                if result == 'yes':            
                    theid = data[0]                
                    obj.Delete_pasanger_pk(theid)
                else:
                    pass


        #Update and Delete buttons
        updatepassanger_btn=Button(Frame_Records,text="Update",bg="white",fg="black",font=("times new roman",15),command=UpdatePassanger)
        updatepassanger_btn.place(x=130,y=130,width=100,height=25) 

        delete_passanger=Button(Frame_Records,text="Delete",bg="white",fg="black",font=("times new roman",15),command=DeletePassanger)
        delete_passanger.place(x=250,y=130,width=100,height=25)


        txt_search=Entry(Frame_Records,font=("times new roman",15),bg="white")
        txt_search.place(x=750,y=130,width=250,height=25)                
        search_btn=Button(Frame_Records,text="Search",bg="white",fg="black",font=("times new roman",15),command=search_function_btn)
        search_btn.place(x=1010,y=130,width=100,height=25)
                
        #Search bind when a key relase
        txt_search.bind('<KeyRelease>',search_function) 

        root.mainloop()