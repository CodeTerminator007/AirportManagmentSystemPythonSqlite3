import sqlite3 
import datetime

class Datbase:
    def __init__(self):
        return

    def Create_database(self):
        conn = sqlite3.connect('database.db')
        conn.close()

    def create_users_table(self):
        conn = sqlite3.connect('database.db')        
        currsor = conn.cursor()
        currsor.execute("""CREATE TABLE users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,            
            first_name text NOT NULL,
            last_name text NOT NULL,
            username text NOT NULL UNIQUE, 
            email text NOT NULL UNIQUE,
            password text NOT NULL,
            datecreated timestamp NOT NULL 
        )
        """)        
        conn.commit()
        conn.close()  

    def create_flights_table(self):
        conn = sqlite3.connect('database.db')        
        currsor = conn.cursor()
        currsor.execute("""CREATE TABLE flights(
            flightid INTEGER PRIMARY KEY ,
            airline_name text NOT NULL,
            flight_number text NOT NULL,
            no_of_seats int NOT NULL,
            no_of_seats_avaliable int,
            source text NOT NULL,                        
            destination text NOT NULL,
            timedate_departure timestamp NOT NULL ,
            timedate_arrival timestamp NOT NULL,
            created timestamp NOT NULL
        )
        """)        
        conn.commit()
        conn.close()

    def create_passengers_table(self):
        conn = sqlite3.connect('database.db')        
        currsor = conn.cursor()
        currsor.execute("""CREATE TABLE passengers(
            passengerid INTEGER PRIMARY KEY ,
            first_name text NOT NULL,
            last_name text NOT NULL,
            email text ,
            cnic int,
            date_of_birth timestamp NOT NULL,                        
            nationality text NOT NULL,
            gender text NOT NULL ,
            flight_number text NOT NULL,
            flightid int NOT NULL,
            created timestamp NOT NULL,            
            FOREIGN KEY(flightid) REFERENCES flights (flightid)            

        );
        """)        
        conn.commit()
        conn.close()

    def Insert_data_passengers(self,first_name,last_name,email,cnic,date_of_birth,nationality,gender,flight_number,flightid,created):

        try:
            conn = sqlite3.connect('database.db')
            currsor = conn.cursor()

            insert_with_param = """INSERT INTO passengers 
                            (
                            'first_name',
                            'last_name',
                            'email',
                            'cnic',
                            'date_of_birth',
                            'nationality',
                            'gender',
                            'flight_number',
                            'created',
                            'flightid'
                            
                            ) 
                            VALUES ( ?,?,?,?,?,?,?,?,?,?);"""

            data_tuple = (
                first_name,
                last_name,
                email,
                cnic,
                date_of_birth,
                nationality,
                gender,
                flight_number,
                created ,
                flightid
                           
            )

            currsor.execute(insert_with_param, data_tuple)
            conn.commit()
            print("Data Inserted in passangers Table..")


        except sqlite3.Error as error:
            print(f"Error in sqlite3 {error}")

        finally:
            if(conn):
                conn.close()
                #closing the connection to database              


    def Insert_data_users(self,first_name,last_name,username,email,password,datecreated):
        try:
            conn = sqlite3.connect('database.db')
            currsor = conn.cursor()

            insert_with_param = """INSERT INTO users 
                            (
                            'first_name',
                            'last_name',
                            'username',
                            'email',
                            'password',
                            'datecreated') 
                            VALUES ( ?, ?,?,?, ?, ?);"""

            data_tuple = (first_name, last_name,username, email, password, datecreated)
            currsor.execute(insert_with_param, data_tuple)
            conn.commit()
            print("Data Inserted in User Table..")


        except sqlite3.Error as error:
            print(f"Error in sqlite3 {error}")

        finally:
            if(conn):
                conn.close()
                #closing the connection to database   

    def Insert_data_flights(self,airline_name,flight_number,no_of_seats,no_of_seats_avaliable,source,destination,timedate_departure,timedate_arrival,created):
        try:
            conn = sqlite3.connect('database.db')
            currsor = conn.cursor()

            insert_with_param = """INSERT INTO flights 
                            (
                            'airline_name',
                            'flight_number',
                            'no_of_seats',
                            'no_of_seats_avaliable',
                            'source',
                            'destination',
                            'timedate_departure',
                            'timedate_arrival',
                            'created'
                            ) 
                            VALUES ( ?, ?,?, ?, ?,?, ?, ?,?);"""

            data_tuple = (
                airline_name,
                flight_number,
                no_of_seats,
                no_of_seats_avaliable,
                source,
                destination,
                timedate_departure,
                timedate_arrival,
                created            
            )

            currsor.execute(insert_with_param, data_tuple)
            conn.commit()
            print("Data Inserted in Flights Table..")


        except sqlite3.Error as error:
            print(f"Error in sqlite3 {error}")

        finally:
            if(conn):
                conn.close()
                #closing the connection to database              

    def Show_data(self):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM users")
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas                 

    def Delete_data(self):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        query = """ DELETE FROM users WHERE userid = 1""" 
        currsor.execute(query)
        conn.commit()
        conn.close()         

obj = Datbase()
# obj.Create_database()
# obj.create_users_table()
# obj.create_flights_table() 
# obj.create_passengers_table()
# obj.Insert_data_flights("PIA","N1233",155,134,"Lahore","London",datetime.datetime(2020,2,22,1,15,00),datetime.datetime(2020,2,22,12,00,00),datetime.datetime.now())
# obj.Insert_data_users("Hussnain",'Ahmad','admin2',"aliahmad522@gmail.com","admin",datetime.datetime.now())
# obj.Insert_data_passengers("Husnain","Ahmad","aliahmad512@gmail.com",12456786,datetime.datetime(1997,2,12),"Pakistani","Male","nh122",datetime.datetime.now(),'2')
# obj.Delete_data()
# obj.Show_data()
    


