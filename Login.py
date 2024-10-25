from tkinter import *
import pymysql
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

#functions

def forget_pass():
    # forget_window = Tk()
    # forget_window.title("Forget Password")
    # forget_window.geometry("800x600")
    # forget_window.resizable(False,False)


    # bgPic = ImageTk.PhotoImage(file='cal.webp')

    # bglbl= Label(forget_window,image=bgPic)
    # bglbl.grid(row=0,column=0)

    # forget_window.mainloop()
    login_window.destroy()
    import forget

def login_user():
    if username.get()== ''or password.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con= mysql.connector.connect(host='localhost',user='root',password='Ankan123123')
            mycursor= con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue, Please try Again!')
            return
        
        query= 'create database if not exists myuserdata'
        mycursor.execute(query)
        query='use myuserdata'
        mycursor.execute(query)
        query= 'select * from datas where username=%s and password= %s'
        mycursor.execute(query,(username.get(),password.get()))
        row= mycursor.fetchone()

        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            login_window.destroy()
            import main


def user_enter(event):
# def on_enter():
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
# def on_enter():
    if PasswordEntry.get()=='Password':
        PasswordEntry.delete(0,END)

def hide():
    openeye.config(file='closeeye.png')
    PasswordEntry.config(show='*')
    eyebutton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    PasswordEntry.config(show='')
    eyebutton.config(command=hide)

def signup_page():
    login_window.destroy()
    import signup



#gui part

login_window = Tk()
login_window.title('Log In')
# login_window.resizable(0,0)
login_window.geometry("1500x660+50+50")
# login_window.minsize(700,500)

#variables
username = StringVar()
password= StringVar()

bgImage = ImageTk.PhotoImage(file='bag.png')

bgLbl = Label(login_window,image=bgImage)
bgLbl.place(x=220,y=20)

heading= Label(login_window,text='USER LOGIN', font=('Microsoft Yahei UI Light',20,'bold'),bg="firebrick1",fg='white')
heading.place(x=950,y=150)

usernameEntry= Entry(login_window,width=25,textvariable=username,font=('Microsoft Yahei UI, Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=895,y=230)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>', user_enter)

Frame(login_window,width=250,height=2,bg='firebrick1').place(x=895,y=250)

PasswordEntry= Entry(login_window,textvariable=password,width=25,font=('Microsoft Yahei UI, Light',11,'bold'),bd=0,fg='firebrick1')
PasswordEntry.place(x=895,y=310)
PasswordEntry.insert(0,'Password')
PasswordEntry.bind('<FocusIn>', password_enter)

Frame(login_window,width=250,height=2,bg='firebrick1').place(x=895,y=330)

openeye= PhotoImage(file='openeye.png')
eyebutton = Button(login_window,image=openeye, bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(x=1130,y=305)

forgotbutton = Button(login_window,text='Forgot Password?', bd=0,bg='white',activebackground='white',cursor='hand2', font=('Microsoft Yahei UI, Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgotbutton.place(x=1070,y=350)

loginButton = Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='white',activeforeground='firebrick1',cursor='hand2',bd=0,width=21, command= login_user)
loginButton.place(x=890,y=400)

orLbl= Label(login_window,text='------------------OR------------------',font=('Open Sans',14,'bold'),fg='firebrick1',bg='white')
orLbl.place(x=905,y=490)


facebook= ImageTk.PhotoImage(file='facebook.png')
fbButton = Button(login_window,image=facebook, bd=0,cursor='hand2')
fbButton.place(x=920,y=540)

twitter= ImageTk.PhotoImage(file='twitter.png')
twitterButton = Button(login_window,image=twitter, bd=0,cursor='hand2',bg="white")
twitterButton.place(x=1020,y=542)

Gmail= ImageTk.PhotoImage(file='gmail.png')
mailButton = Button(login_window,image=Gmail, bd=0,cursor='hand2',bg='white')
mailButton.place(x=1120,y=540)

signupLbl= Label(login_window,text='Do not have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLbl.place(x=880,y=590)

newaccount = Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',bd=0,width=21,command=signup_page)
newaccount.place(x=1050,y=590)





login_window.mainloop()
