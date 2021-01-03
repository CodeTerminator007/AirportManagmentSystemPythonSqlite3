from database import *

obj = Datbase()
avaliable_flights = obj.Show_all_flights_data()
aval_destination = []
for f in avaliable_flights:
    blackflag = False
    city = f[6]
    for g in aval_destination:
        if city == g:
            blackflag = True
    
    if blackflag == False:
        aval_destination += [city]
