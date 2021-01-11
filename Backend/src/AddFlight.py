from tkinter import *
from database import Database
import datetime
import tkinter.messagebox as tkMessageBox



class ADD_FLIGHT:
    def __init__(self):
        pass 

    def view(self):
        obj = Database()
        root=Tk()
        root.title("Add Flight")
        root.geometry("1199x800+100+1") 

        def close():
            root.destroy()

        Create_Flight_Frame=Frame(root,bg="white")
        Create_Flight_Frame.place(relx=0.5,rely=0.5, anchor = CENTER ,height=650,width=800)
        
        title =Label(Create_Flight_Frame,text="Add Flight ",font=("Impact",35,"bold"),fg="black",bg="white")
        title.place(x=90,y=30)

        lbl_Airline_name=Label(Create_Flight_Frame,text="Airline Name",
        font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_Airline_name.place(x=90,y=140)
        txt_Airline_name=Entry(Create_Flight_Frame,font=("times new roman",15),bg="white")
        txt_Airline_name.place(x=90,y=170,width=250,height=30)
        
        lbl_Flight_number=Label(Create_Flight_Frame,text="Flight Number",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_Flight_number.place(x=450,y=140)
        txt_Flight_number=Entry(Create_Flight_Frame,font=("times new roman",15),bg="white")
        txt_Flight_number.place(x=450,y=170,width=250,height=30)
        
        lbl_seats=Label(Create_Flight_Frame,text="Total Seats",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_seats.place(x=90,y=220)
        txt_seats=Entry(Create_Flight_Frame,font=("times new roman",15),bg="white")
        txt_seats.place(x=90,y=250,width=250,height=30)
        
        lbl_avaliable_seats=Label(Create_Flight_Frame,text="Availiable Seats",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_avaliable_seats.place(x=450,y=220)
        txt_avaliable_seats=Entry(Create_Flight_Frame,font=("times new roman",15),bg="white")
        txt_avaliable_seats.place(x=450,y=250,width=250,height=30)
        
                        
        lbl_From=Label(Create_Flight_Frame,text="Location From",font=("Goudy old style",15,"bold"),
        fg="black",bg="white")
        lbl_From.place(x=90,y=300)

        txt_From =Entry(Create_Flight_Frame,font=("times new roman",15),bg="white")
        txt_From.place(x=90,y=330,width=250,height=30)


        lbl_TO=Label(Create_Flight_Frame,text="Location To",font=("Goudy old style",15,"bold"),
        fg="black",bg="white")
        lbl_TO.place(x=450,y=300)

        txt_To=Entry(Create_Flight_Frame,font=("times new roman",15),bg="white")
        txt_To.place(x=450,y=330,width=250,height=30)


        lbl_arrival_time = Label(Create_Flight_Frame,text="Arrival Time",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_arrival_time.place(x=90,y=400)
        arrival_time=Entry(Create_Flight_Frame,font=("times new roman",13),bg="white")
        arrival_time.place(x=90,y=430,width=250,height=30)
        arrival_time.insert(END, "12/01/2021 12:15:00")


        lbl_departure_time = Label(Create_Flight_Frame,text="Departure Time",font=("Goudy old style",15,"bold"),fg="black",bg="white")
        lbl_departure_time.place(x=450,y=400)
        departure_time=Entry(Create_Flight_Frame,font=("times new roman",13),bg="white")
        departure_time.place(x=450,y=430,width=250,height=30)
        departure_time.insert(END, "12/01/2021 12:15:00")

        def datemaskarrival(event):
            if len(arrival_time.get()) == 2:
                arrival_time.insert(END,"/")
            elif len(arrival_time.get()) == 5:
                arrival_time.insert(END,"/")
            elif len(arrival_time.get()) == 8:
                arrival_time.insert(END, " ")
            elif len(arrival_time.get()) == 11:
                arrival_time.insert(END, ":")                                
            elif len(arrival_time.get()) == 14:
                arrival_time.insert(END, ":")
            elif len(arrival_time.get()) == 18:
                arrival_time.delete(17, END)                 

                

        def datemaskdeparture(event):
            if len(departure_time.get()) == 2:
                departure_time.insert(END,"/")
            elif len(departure_time.get()) == 5:
                departure_time.insert(END,"/")
            elif len(departure_time.get()) == 8:
                departure_time.insert(END, " ")
            elif len(departure_time.get()) == 11:
                departure_time.insert(END, ":")                                
            elif len(departure_time.get()) == 14:
                departure_time.insert(END, ":")
            elif len(departure_time.get()) == 18:
                departure_time.delete(17, END)               


        #binding both time entry fields
        arrival_time.bind('<KeyRelease>', datemaskarrival)     
        departure_time.bind('<KeyRelease>', datemaskdeparture)     
 
        def submit():

            #Getting Values
            Airline_Name = txt_Airline_name.get()
            Flight_number = txt_Flight_number.get()
            Seats = txt_seats.get()
            Seats_Availiable = txt_avaliable_seats.get()
            Location_From = txt_From.get()
            Location_To  = txt_To.get()
            Arrival_time= arrival_time.get() 
            Departure_time =departure_time.get() 

            #Defining Boolean Values 
            BlackFlag1 = False
            BlackFlag2 = False
            BlackFlag3 = False
            BlackFlag4 = False
            BlackFlag5 = False
            BlackFlag6 = False


            #if Conditions to check if input data is Empty
            if Airline_Name =='':
                dot=Label(Create_Flight_Frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=170)
                BlackFlag1 = True
            if Flight_number =='':
                dot=Label(Create_Flight_Frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=420,y=170)
                BlackFlag2 = True
            if Seats =='':
                dot=Label(Create_Flight_Frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=250)
                BlackFlag3 = True
            if Seats_Availiable =='':
                dot=Label(Create_Flight_Frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=420,y=250)
                BlackFlag4 = True
            if Location_From =='':
                dot=Label(Create_Flight_Frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=330)
                BlackFlag5 = True
            if Location_To =='':
                dot=Label(Create_Flight_Frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=420,y=330)
                BlackFlag6 = True
            if Arrival_time =='':
                dot=Label(Create_Flight_Frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=60,y=430)
                BlackFlag6 = True
            else:
                Arrival_time_obj = datetime.datetime.strptime(Arrival_time, '%d/%m/%y %H:%M:%S')

            if Departure_time =='':
                dot=Label(Create_Flight_Frame,text="*",font=("Goudy old style",20,"bold"),
                fg="red",bg="white")
                dot.place(x=420,y=430)
                BlackFlag6 = True
            else:
                Departure_time_obj = datetime.datetime.strptime(Departure_time, '%d/%m/%y %H:%M:%S')                                 


            #Checking if there is an empty entered value
            if BlackFlag1 == False and BlackFlag2 ==False and BlackFlag3 == False and BlackFlag4 == False and BlackFlag5 == False and BlackFlag6 ==False:
                created_time = datetime.datetime.now()
                obj.Insert_data_flights(Airline_Name,Flight_number,int(Seats),int(Seats_Availiable),Location_From,Location_To,Departure_time_obj,Arrival_time_obj,created_time)
                tkMessageBox.showwarning('', 'Flight Created!', icon="warning" ,parent=Create_Flight_Frame)                 
                close()
            else:
                tkMessageBox.showwarning('', 'Looks Like Some Data is Missing .!', icon="warning" ,parent=Create_Flight_Frame) 

            

        submit_btn=Button(Create_Flight_Frame,text="Submit", command=submit , bg="white",fg="black",font=("times new roman",15))
        submit_btn.place(x=90,y=540,width=180,height=40)
        root.mainloop()

