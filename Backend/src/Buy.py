from tkinter import *
import smtplib
from tkcalendar import  DateEntry
import re 
import tkinter.messagebox as tkMessageBox

#files import
from database import *



class Buy_Tickets:
    def __init__(self):
        pass 

    def buy(self):
        obj = Database()
        root=Tk()
        root.title("Airport Managment System : Buy Ticket")
        root.geometry("1199x800+100+1") 

        def close():
            root.destroy()

        Buy_ticket_frame=Frame(root,bg="white")
        Buy_ticket_frame.place(relx=0.5,rely=0.5, anchor = CENTER ,height=650,width=800)
        
        title =Label(Buy_ticket_frame,text="Passenger Information",font=("Impact",35,"bold"),fg="black",bg="white")
        title.place(relx=0.2,y=30)

        lbl_first_name=Label(Buy_ticket_frame,text="First Name",
        font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_first_name.place(x=90,y=140)
        txt_first_name=Entry(Buy_ticket_frame,font=("times new roman",15),bg="white")
        txt_first_name.place(x=90,y=170,width=250,height=30)
        
        lbl_last_name=Label(Buy_ticket_frame,text="Last Name",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_last_name.place(x=450,y=140)
        txt_last_name=Entry(Buy_ticket_frame,font=("times new roman",15),bg="white")
        txt_last_name.place(x=450,y=170,width=250,height=30)
        
        lbl_email=Label(Buy_ticket_frame,text="Email",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_email.place(x=90,y=220)
        txt_email=Entry(Buy_ticket_frame,font=("times new roman",15),bg="white")
        txt_email.place(x=90,y=250,width=250,height=30)
        
        lbl_cnic=Label(Buy_ticket_frame,text="CNIC",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_cnic.place(x=450,y=220)
        txt_cnic=Entry(Buy_ticket_frame,font=("times new roman",15),bg="white")
        txt_cnic.place(x=450,y=250,width=250,height=30)
        
                        
        lbl_birth=Label(Buy_ticket_frame,text="Date of birth",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_birth.place(x=90,y=300)
        cal = DateEntry(Buy_ticket_frame, width=12, background='white',foreground='black', borderwidth=2, year=1997)
        cal.place(x=90,y=330,width=250,height=30)


        lbl_nationality=Label(Buy_ticket_frame,text="Nationality",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_nationality.place(x=450,y=300)
        txt_nationality=Entry(Buy_ticket_frame,font=("times new roman",15),bg="white")
        txt_nationality.place(x=450,y=330,width=250,height=30)


        lbl_gender=Label(Buy_ticket_frame,text="Gender",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_gender.place(x=90,y=380)        
        selector = StringVar(Buy_ticket_frame)
        male = Radiobutton( Buy_ticket_frame, text="Male",variable=selector , value="Male")
        male.place(x=90,y=410)
        male.select()
        female=Radiobutton(Buy_ticket_frame,text="Female",variable=selector , value="Female")
        female.place(x=200,y=410)

        #To Get The Cities List Flights are Going
        avaliable_flights = obj.Show_all_flights_data()
        aval_destination = []
        for f in avaliable_flights:
            cityflag = False
            city = f[6]
            for g in aval_destination:
                if city == g:
                    cityflag = True
            
            if cityflag == False:
                aval_destination += [city]


        Destination_label=Label(Buy_ticket_frame,text="Destination",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        Destination_label.place(x=450,y=380)
        clicked = StringVar(Buy_ticket_frame)
        clicked.set("Select Here")
        drop_down_destinations= OptionMenu(Buy_ticket_frame, clicked, 'Chose Here',*aval_destination)
        drop_down_destinations.place(x=450,y=410,width=250,height=30)


        def show_availiable_flights():
            location = clicked.get()
            if location == 'Select Here' or location =='Chose Here':
                tkMessageBox.showwarning('', 'Select a Destination ', icon="warning",parent=Buy_ticket_frame)
            else:
                flight = []
                avaliable_flights_list =  obj.show_specif_flight_data_with_destination(location)
                for x in avaliable_flights_list:
                    id = x[0]
                    flight_name = x[2]
                    flight_num = x[1]
                    flight_time = x[7]
                    flight += [f"{id} {flight_name} {flight_num} leaves on {flight_time}"]
                    
                drop_down_flights=OptionMenu(Buy_ticket_frame,clicked2,'Select Flights Here',*flight )        
                drop_down_flights.place(x=350,y=540,width=350,height=30)



        Avaliable_flights_label=Label(Buy_ticket_frame,text="Avaliable Flights",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        Avaliable_flights_label.place(x=350,y=500)
        refresh_btn=Button(Buy_ticket_frame,text="Refresh",bg="white",fg="black", command=show_availiable_flights, font=("times new roman",15))
        refresh_btn.place(x=520,y=505,width=90,height=20)
        clicked2 = StringVar(Buy_ticket_frame)
        clicked2.set("Select Here")
        drop_down_flights=OptionMenu(Buy_ticket_frame, clicked2, "default")        
        drop_down_flights.place(x=350,y=540,width=350,height=30)

        def send_mail(address,first_name,last_name,flight_name,flight_num , flight_time ):            
            from usernamepassword import EMAIL_ADDRESS , EMAIL_PASSWORD

            with smtplib.SMTP('smtp.gmail.com',587 ) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)

                subject = 'Airport Ticket'
                body = f'Hi {first_name} {last_name } This The Ticket has been confirmed and the Plane {flight_name} {flight_num} Will leave on {flight_time} Thanks for chosing us \n Regards Hussnain Ahmad '

                msg = f"Subject:{subject}\n\n {body}"
                smtp.sendmail(EMAIL_ADDRESS,address , msg)


        def Submit():
            global email

            #Getting Values      
            first_name = txt_first_name.get()
            last_name = txt_last_name.get()
            unvalidated_email = txt_email.get()                
            unvalidated_cnic = txt_cnic.get()
            date_of_birth = cal.get_date()
            nationality = txt_nationality.get()
            gender = selector.get()
            flight = clicked2.get()
            flight_name = ""
            flight_number = ""          
            created = datetime.datetime.now()

            #Defining Boolean Values
            blackflag1 =False
            blackflag2 =False 
            blackflag3 =False 
            blackflag4 = False 
            blackflag5 =False 
            blackflag6 =False 
            blackflag7  =False 
            blackflag8 = False


            #if Conditions to check if input data is Empty
            if first_name == '':
                dot=Label(Buy_ticket_frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=170)
                blackflag1 = True
            if last_name == '':
                dot=Label(Buy_ticket_frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=420,y=170)
                blackflag2 = True
            regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
            if re.search(regex,unvalidated_email):
                email = unvalidated_email
            else:
                dot=Label(Buy_ticket_frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=250)
                blackflag3 = True
            regex_cnic = '^[0-9]\w{8,13}$'      
            if re.search(regex_cnic,unvalidated_cnic):
                cnic= unvalidated_cnic
            else:
                dot=Label(Buy_ticket_frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=420,y=250)
                blackflag4 = True

            if date_of_birth == '':
                dot=Label(Buy_ticket_frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=330)
                blackflag5 = True 
            if nationality == '':
                dot=Label(Buy_ticket_frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=420,y=330)
                blackflag6 = True
            if gender =='':
                dot=Label(Buy_ticket_frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=410) 
                blackflag7 = True           
            if flight=='Select Here' or flight =='Select Flights Here':
                dot=Label(Buy_ticket_frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=330,y=500)  
                blackflag8 = True
            else:
                flightid = int(flight[0])
                real_flight = obj.show_specif_flight_data_with_pk(flightid)
                for s in real_flight:
                    flight_number = s[2]
                    flight_name = s[1]
                    flight_time = s[7]  
                    aval_seats = s[4]                    
                                     


            #Checking if there is an empty entered value                
            if blackflag1 ==False and blackflag2 ==False and blackflag3==False and blackflag4 == False and blackflag5==False and blackflag6 == False and blackflag7 == False and blackflag8 == False:
                if aval_seats >= 1 :
                    result = tkMessageBox.askquestion('','Confirm the ticket', icon="warning",parent=Buy_ticket_frame)     
                    if result == 'yes':            
                        obj.Insert_data_passengers(first_name,last_name,email,cnic,date_of_birth,nationality,gender,flight_number,created,flightid)
                        obj.update_flight_avaliable_seats(flightid,aval_seats)
                        send_mail(email,first_name,last_name,flight_name,flight_number,flight_time)
                        close()  
                else:
                    tkMessageBox.showwarning('', 'No seats Avaliable ', icon="warning",parent=Buy_ticket_frame)
            else:
                    tkMessageBox.showwarning('', 'Looks Like Some Data is Missing .!', icon="warning" ,parent=Buy_ticket_frame) 



        submit_btn=Button(Buy_ticket_frame,text="Submit", command=Submit, bg="white",fg="black",font=("times new roman",15))
        submit_btn.place(x=90,y=540,width=180,height=40)
        root.mainloop()
