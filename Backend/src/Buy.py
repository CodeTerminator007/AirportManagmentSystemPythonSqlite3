from tkinter import*
from tkinter import ttk
import smtplib
import os
from database import *
from tkcalendar import  DateEntry
import avaliable_destinations
class Buy_Tickets:
    def __init__(self):
        pass

    def buy(self ):
        obj = Datbase()
        root=Tk()
        root.title("Passenger Information")
        root.geometry("1199x600+100+50")        

        #BuyTicket Information
        Buy_ticket_frame=Frame(root,bg="white")
        Buy_ticket_frame.place(relx=0.5,rely=0.5, anchor = CENTER ,height=650,width=800)
        
        title =Label(Buy_ticket_frame,text="Passenger Information",font=("Impact",35,"bold"),fg="black",bg="white")
        title.place(x=90,y=30)

        lbl_first_name=Label(Buy_ticket_frame,text="First Name",font=("Goudy old style",15,"bold"),fg="black",bg="white")
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
        
                        
        lbl_birth=Label(Buy_ticket_frame,text="Date of birth",font=("Goudy old style",15,"bold"),
        fg="black",bg="white")
        lbl_birth.place(x=90,y=300)
        cal = DateEntry(Buy_ticket_frame, width=12, background='white',
                            foreground='white', borderwidth=2, year=2010)
        cal.place(x=90,y=330,width=250,height=30)


        lbl_nationality=Label(Buy_ticket_frame,text="Nationality",font=("Goudy old style",15,"bold"),
        fg="black",bg="white")
        lbl_nationality.place(x=450,y=300)
        txt_nationality=Entry(Buy_ticket_frame,font=("times new roman",15),bg="white")
        txt_nationality.place(x=450,y=330,width=250,height=30)


        lbl_gender=Label(Buy_ticket_frame,text="Gender",font=("Goudy old style",15,"bold"),
        fg="black",bg="white")
        lbl_gender.place(x=90,y=380)
        
        selector = StringVar(Buy_ticket_frame)
        male = Radiobutton( Buy_ticket_frame, text="Male", variable=selector , value="Male")
        male.place(x=90,y=410)
        female=Radiobutton(Buy_ticket_frame,text="Female",variable=selector , value="Female")
        female.place(x=200,y=410)


        Destination_label=Label(Buy_ticket_frame,text="Destination",font=("Goudy old style",15,"bold"),
        fg="black",bg="white")
        Destination_label.place(x=450,y=380)
        clicked = StringVar(Buy_ticket_frame)
        clicked.set("select Here")
        drop_down_destinations=OptionMenu(Buy_ticket_frame, clicked, *avaliable_destinations.aval_destination)
        drop_down_destinations.place(x=450,y=410,width=250,height=30)


        def check():
            s = clicked.get()
            flight = []
            avaliable_flights_list =  obj.show_specif_flight_data(s)
            for x in avaliable_flights_list:
                id = x[0]
                flight_name = x[2]
                flight_num = x[1]
                flight_time = x[7]
                flight += [f"{id} {flight_name} {flight_num} leaves on {flight_time}"]
                
            drop_down_flights=OptionMenu(Buy_ticket_frame, clicked2, *flight)        
            drop_down_flights.place(x=90,y=490,width=250,height=30)



        Avaliable_flights_label=Label(Buy_ticket_frame,text="Avaliable Flights",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        Avaliable_flights_label.place(x=90,y=460)
        refresh_btn=Button(Buy_ticket_frame,text="",bg="white",fg="black",command=check, font=("times new roman",15))
        refresh_btn.place(x=250,y=460,width=30,height=20)
        clicked2 = StringVar(Buy_ticket_frame)
        clicked2.set("select Here")
        drop_down_flights=OptionMenu(Buy_ticket_frame, clicked2, "default")        
        drop_down_flights.place(x=90,y=490,width=250,height=30)

        def send_mail(address):            
            EMAIL_ADDRESS = ''
            EMAIL_PASSWORD = ''

            with smtplib.SMTP('smtp.gmail.com',587 ) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)

                subject = 'Airport Ticket'
                body = 'Hi This The Ticket has been confirmed by'

                msg = f"Subject:{subject}\n\n {body}"
                smtp.sendmail(EMAIL_ADDRESS,address , msg)
                
        def confirm_ticket():
            first_name = txt_first_name.get()
            last_name = txt_last_name.get()
            email = txt_email.get()
            cnic = int(txt_cnic.get())
            date_of_birth = cal.get_date()
            nationality = txt_nationality.get()
            gender = selector.get()
            flight = clicked2.get()
            flightid = int(flight[0])
            real_flight = obj.show_specif_flight_data_with_pk(flightid)
            for s in real_flight:
                flight_number = s[2]                
            created = datetime.datetime.now()
            # print(flight_number)
            obj.Insert_data_passengers(first_name,last_name,email,cnic,date_of_birth,nationality,gender,flight_number,created,flightid)
            send_mail(email)
            val = obj.Show_all_passangers_data()

        submit_btn=Button(Buy_ticket_frame,text="Submit", command=confirm_ticket, bg="white",fg="black",font=("times new roman",15))
        submit_btn.place(x=90,y=540,width=180,height=40)
        root.mainloop()
