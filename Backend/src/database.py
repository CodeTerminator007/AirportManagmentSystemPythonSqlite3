import datetime
import sqlite3


class Database:
    def __init__(self):
        return

    def Create_database(self):
        conn = sqlite3.connect('database.db')
        conn.close()


                                            #Functions To Create Tables     
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
            datecreated timestamp NOT NULL,
            updatedtime timestamp NOT NULL 
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
            flight_number text NOT NULL UNIQUE,
            no_of_seats int NOT NULL,
            no_of_seats_avaliable int,
            source text NOT NULL,                        
            destination text NOT NULL ,
            timedate_departure timestamp NOT NULL ,
            timedate_arrival timestamp NOT NULL,
            created timestamp NOT NULL,
            updatedtime timestamp NOT NULL
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
            email text NOT NULL,
            cnic text UNIQUE,
            date_of_birth timestamp NOT NULL,                        
            nationality text NOT NULL,
            gender text NOT NULL ,
            flight_number text NOT NULL,
            flightid int NOT NULL,
            created timestamp NOT NULL,
            updatedtime timestamp NOT NULL,            
            FOREIGN KEY(flightid) REFERENCES flights (flightid)            

        );
        """)
        conn.commit()
        conn.close()


                                            #Functions To Insert Data in Tables
    def Insert_data_passengers(self, first_name, last_name, email, cnic, date_of_birth, nationality, gender, flight_number, created, flightid):

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
                            'flightid',
                            'updatedtime'

                            ) 
                            VALUES ( ?,?,?,?,?,?,?,?,?,?,?);"""
            updatedtime = datetime.datetime.now()
            data_tuple = (
                first_name,
                last_name,
                email,
                cnic,
                date_of_birth,
                nationality,
                gender,
                flight_number,
                created,
                flightid,
                updatedtime

            )

            currsor.execute(insert_with_param, data_tuple)
            conn.commit()

        except sqlite3.Error as error:
            print(f"Error in sqlite3 {error}")

        finally:
            if(conn):
                conn.close()

    def Insert_data_users(self, first_name, last_name, username, email, password, datecreated):
        try:
            conn = sqlite3.connect('database.db')
            currsor = conn.cursor()
            updatedtime = datetime.datetime.now()
            insert_with_param = """INSERT INTO users 
                            (
                            'first_name',
                            'last_name',
                            'username',
                            'email',
                            'password',
                            'datecreated',
                            updatedtime            

                            ) 
                            VALUES ( ?, ?,?,?, ?, ?,?);"""

            data_tuple = (first_name, last_name, username, email,
                          password, datecreated, updatedtime)
            currsor.execute(insert_with_param, data_tuple)
            conn.commit()

        except sqlite3.Error as error:
            print(f"Error in sqlite3 {error}")

        finally:
            if(conn):
                conn.close()

    def Insert_data_flights(self, airline_name, flight_number, no_of_seats, no_of_seats_avaliable, source, destination, timedate_departure, timedate_arrival, created):
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
                            'created',
                            'updatedtime'
                            ) 
                            VALUES ( ?, ?,?, ?, ?,?, ?, ?,?,?);"""
            updatedtime = datetime.datetime.now()
            data_tuple = (
                airline_name,
                flight_number,
                no_of_seats,
                no_of_seats_avaliable,
                source,
                destination,
                timedate_departure,
                timedate_arrival,
                created,
                updatedtime
            )

            currsor.execute(insert_with_param, data_tuple)
            conn.commit()
            print("Data Inserted in Flights Table..")

        except sqlite3.Error as error:
            print(f"Error in sqlite3 {error}")

        finally:
            if(conn):
                conn.close()
                                            #Functions To Show Data in Tables
    def Show_all_users_data(self):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM users")
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def show_specif_user_data(self, pk):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM users WHERE userid = ? ", [pk])
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def Show_all_flights_data(self):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM flights")
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def search_specif_flight_data(self, entry):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute(
            "SELECT * FROM flights WHERE destination LIKE ? COLLATE NOCASE OR flight_number LIKE ? COLLATE NOCASE OR airline_name LIKE ? COLLATE NOCASE or source LIKE ? COLLATE NOCASE", ["%"+entry+"%", "%"+entry+"%", "%"+entry+"%","%"+entry+"%"])
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def search_specif_passanger_data(self, search):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute(
            "SELECT * FROM passengers WHERE first_name LIKE ? COLLATE NOCASE OR flight_number LIKE ? COLLATE NOCASE OR last_name LIKE ?  COLLATE NOCASE OR nationality like ? COLLATE NOCASE OR email LIKE ? COLLATE NOCASE OR cnic LIKE ? COLLATE NOCASE", ["%"+search+"%", "%"+search+"%", "%"+search+"%","%"+search+"%","%"+search+"%","%"+search+"%"])
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def show_specif_flight_data_with_pk(self, pk):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM flights WHERE flightid = ?", [pk])
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas
    def show_specif_flight_data_with_flightnumber(self, flnumber):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM flights WHERE flight_number = ?", [flnumber])
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def show_specif_flight_data_with_destination(self,destination):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM flights WHERE destination = ?", [destination])
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas                

    def Show_all_passangers_data(self):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM passengers")
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def show_specif_passanger_data(self, pk):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("SELECT * FROM passengers WHERE passengerid = ?", [pk])
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

                                                #Functions To Update Tables

    def update_flight_avaliable_seats(self, pk, avl_seats):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        rem_seats = avl_seats - 1
        currsor.execute(
            "Update flights set no_of_seats_avaliable = ? Where flightid = ?", [rem_seats, pk])
        datas = currsor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def update_flight_with_pk(self, pk, companyname, flightnumber, totalseats, avalseats, fromwhere, towhere, departuretime, arrivaltime):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        updatetime = datetime.datetime.now()
        currsor.execute("Update flights set airline_name = ? , flight_number=? ,  no_of_seats=? , no_of_seats_avaliable=? , source = ? ,destination = ?, timedate_departure = ?, timedate_arrival = ?, updatedtime = ? WHERE flightid = ? ", [
                        companyname, flightnumber, totalseats, avalseats, fromwhere, towhere, departuretime, arrivaltime, updatetime, pk])
        conn.commit()
        conn.close()



    def update_passanger_with_pk(self, pk, first_name, last_name, email, cnic, date_of_birth, nationality,flightid,flightnum):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        updatetime = datetime.datetime.now()
        currsor.execute("Update passengers set first_name = ? , last_name=? , email = ?, cnic=? , date_of_birth=? , nationality = ? ,flightid = ?,flight_number = ? , updatedtime = ? WHERE passengerid = ? ",
        [first_name, last_name, email, cnic, date_of_birth, nationality,flightid,flightnum,updatetime, pk])
        conn.commit()
        conn.close()

    def update_user_with_pk(self, pk, first_name, last_name, username, email ,password):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        updatetime = datetime.datetime.now()
        currsor.execute("Update users set first_name = ? , last_name=? , username = ?, email=? ,  password=? ,updatedtime = ?  WHERE userid = ? ",
        [first_name, last_name, username,email, password, updatetime, pk])
        conn.commit()
        conn.close()


                                                #Functions to Delete Data From Tables
    def Delete_flight_pk(self, pk):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("DELETE FROM flights WHERE flightid=?", [pk])
        conn.commit()
        conn.close()

    def Delete_pasanger_pk(self, pk):
        conn = sqlite3.connect('database.db')
        currsor = conn.cursor()
        currsor.execute("DELETE FROM passengers WHERE passengerid=?", [pk])
        conn.commit()
        conn.close()

# obj = Database()
# obj.Insert_data_users('Ali','Ahmad','admin2','Aliahmad631@gmail.com','admin',datetime.datetime.now())