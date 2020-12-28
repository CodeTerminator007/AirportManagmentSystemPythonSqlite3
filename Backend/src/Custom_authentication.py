from database import Datbase
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
                values = obj.Show_data() #calling ShowFunction FROM DATABASECLASS
                for value in values:
                    usern = value[3]
                    passw = value[5]
                    if usern == username and passw == password:
                        print("Logged in")
                        print(value)
                        break
                    else:
                        print("Wrong Username or Password")                  
            else:
                print("Password is Missing")
        else:
            print("User Name is is Missing")