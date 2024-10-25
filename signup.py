from tkinter import *
from PIL import Image , ImageTk
from tkinter import ttk
import pymysql
import mysql.connector
from tkinter import messagebox

#functions
def login_page():
    signup_window.destroy()
    import Login

def clear():
     EmailEntry.delete(0,END)
     UserNameEntry.delete(0,END)
     PasswordEntry.delete(0,END)
     ConfirmPasswordEntry.delete(0,END)
     check.set(0)

def connect_database():
    if email.get() == '' or username.get()=='' or password.get()=='' or cpassword.get()=='':
            messagebox.showerror('Error','All fields are required')
    elif password.get() != cpassword.get():
         messagebox.showerror('Error','Passwords do not match')
    elif check.get()==0:
         messagebox.showerror('Error','Please accept the terms and conditions')
    else:
         try:
            con = mysql.connector.connect(host= 'localhost',user='root',password='Ankan123123')
            mycursor = con.cursor()
         except:
              messagebox("Error", "Database Connectivity issue, please try again")
              return
         
         try:
            query = 'create database if not exists myuserdata'
            mycursor.execute(query)
            query='use myuserdata'
            mycursor.execute(query)
            query= 'create table datas(id int auto_increment primary key not null, email varchar(80), username varchar(100), password varchar(25))'
            mycursor.execute(query)
         except:
               mycursor.execute('use myuserdata')

               # # query= 'select * from datas where username = %s'
               # # mycursor.execute(query,(username.get()))
               # val1 = username.get()
               # mycursor.execute("Select * from datas where `username` like %s ", ("%"+val1+"%"))
               # row1 = mycursor.fetchall()
               # mycursor.execute('select * from datas where username = %s',(username.get()))

               # row1= mycursor.fetchone()

               # # query= 'select * from datas where email = %s'
               # # mycursor.execute(query,(email.get()))
               # mycursor.execute('select * from datas where email = %s',(email.get()))

               # row2= mycursor.fetchone()
               # if len(row1)!= None:
               #      messagebox.showerror('Error', 'Username already exists')
               # elif len(row2)!= None:
               #      messagebox.showerror('Error', 'email already exists')
               # else:

                    # query = 'insert into datas(email,username,password) values(%s,%s,%s)'
                    # mycursor.execute(query,(email.get(),username.get(),password.get()))
               mycursor.execute('insert into datas(email,username,password) values(%s,%s,%s)',(email.get(),username.get(),password.get()))
               con.commit()
               messagebox.showinfo('Success','Registration is Successful')
               con.close()

               clear()# to clear the entry fields
               signup_window.destroy()
               import Login


# GUI

signup_window = Tk()
signup_window.geometry("1500x660+50+50")
# signup_window.resizable(False,False)
signup_window.title('Signup')

#variables
username = StringVar()
password= StringVar()
email = StringVar()
cpassword = StringVar()
background = ImageTk.PhotoImage(file='bag.png')

bgLabel= Label(signup_window,image=background)
bgLabel.place(x=220,y=20)

Inputframe = Frame(signup_window,bd=1,width=390,height=520,bg="white")
Inputframe.place(x=840,y=130)

heading= Label(Inputframe,text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light',22,'bold underline'),bg="white",fg='firebrick1')
heading.place(x=30,y=10)

Email= Label(Inputframe,text='Email', font=('Microsoft Yahei UI Light',9,'bold'),bg="white",fg='firebrick1')
Email.place(x=28,y=80)

EmailEntry= Entry(Inputframe,textvariable=email,width=25,font=('Microsoft Yahei UI, Light',16,'bold'),bd=0,fg='white',bg='firebrick1')
EmailEntry.place(x=28,y=110)

UserName= Label(Inputframe,text='UserName', font=('Microsoft Yahei UI Light',9,'bold'),bg="white",fg='firebrick1')
UserName.place(x=28,y=150)

UserNameEntry= Entry(Inputframe,width=25,textvariable=username,font=('Microsoft Yahei UI, Light',16,'bold'),bd=0,fg='white',bg='firebrick1')
UserNameEntry.place(x=28,y=180)

Password= Label(Inputframe,text='Password', font=('Microsoft Yahei UI Light',9,'bold'),bg="white",fg='firebrick1')
Password.place(x=28,y=220)

PasswordEntry= Entry(Inputframe,textvariable=password,width=25,font=('Microsoft Yahei UI, Light',16,'bold'),bd=0,fg='white',bg='firebrick1')
PasswordEntry.place(x=28,y=250)

ConfirmPassword= Label(Inputframe,text='Confirm Password', font=('Microsoft Yahei UI Light',9,'bold'),bg="white",fg='firebrick1')
ConfirmPassword.place(x=28,y=290)

ConfirmPasswordEntry= Entry(Inputframe,width=25,font=('Microsoft Yahei UI, Light',16,'bold'),bd=0,fg='white',bg='firebrick1',textvariable=cpassword)
ConfirmPasswordEntry.place(x=28,y=320)

check = IntVar()
Terms = Checkbutton(Inputframe,text='I Agree to the terms and Conditions',font=('Microsoft Yahei UI Light',9,'bold'),bg='white',fg='firebrick1',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable= check)
Terms.place(x=28 , y =360)

SignupButton = Button(Inputframe,text='Sign up',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='white',activeforeground='firebrick1',cursor='hand2',bd=0,width=21,command= connect_database)
SignupButton.place(x=40,y=400)

signupLbl= Label(Inputframe,text='Have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLbl.place(x=28,y=470)

loggedin = Button(Inputframe,text='Log in',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',bd=0,width=21,command=login_page)
loggedin.place(x=225,y=470)






signup_window.mainloop()