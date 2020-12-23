from tkinter import*
from database import Datbase
from Custom_authentication import Authentication
root=Tk()
root.title("Login System")
root.geometry("800x600+100+50")
root.bg="Black"
root.resizable(False, False)


class LoginWindow(Datbase):

    #GUI CODE HERE
    Frame_Login=Frame(root,bg="white")
    Frame_Login.place(relx=0.2,rely=0.2,height=380,width=500,)

    title=Label(Frame_Login,text="Login ",font=("Impact",35,"bold"),fg="black",bg="white")
    title.place(x=90,y=30)

    desc=Label(Frame_Login,text="Management Login Area",font=("Goudy old style",15,"bold"),fg="black",bg="white")
    desc.place(x=90,y=100)

    lbl_user=Label(Frame_Login,text="User Name",font=("Goudy old style",15,"bold"),fg="black",bg="white")
    lbl_user.place(x=90,y=140)
    
    txt_user=Entry(Frame_Login,font=("times new roman",15),bg="lightgrey")
    txt_user.place(x=90,y=170,width=350,height=35)

    lbl_pass=Label(Frame_Login,text="Password",font=("Goudy old style",15,"bold"),fg="black",bg="white")
    lbl_pass.place(x=90,y=210)
    
    txt_pass=Entry(Frame_Login,font=("times new roman",15),bg="lightgrey")
    txt_pass.place(x=90,y=240,width=350,height=35)

    forget_btn=Button(Frame_Login,text="forget password",bg="white",fg="black",bd=0,font=("times new roman",12))
    forget_btn.place(x=90,y=280)

    #creating object of Authentication Class
    obj = Authentication(txt_user,txt_pass) 

    login_btn=Button(Frame_Login,text="Login",bg="white",fg="black",font=("times new roman",15),command=obj.check_username_password)
    login_btn.place(x=90,y=320,width=180,height=40)
    
    root.mainloop()

