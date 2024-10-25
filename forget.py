from tkinter import *
import pymysql
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
from PIL import Image , ImageTk

# Functions
def change_password():
    if email.get() == ''or password.get()=='' or cpassword.get()=='':
            messagebox.showerror('Error','All fields are required')
    elif password.get() != cpassword.get():
         messagebox.showerror('Error','Passwords do not match')
    else:
          con= mysql.connector.connect(host='localhost',user='root',password='Ankan123123',database='myuserdata')
          mycursor = con.cursorz()
          query= 'select * from datas where email= %s '
          mycursor.execute(query, (email.get()))
          row= mycursor.fetchone()
          if row == None:
                messagebox.showerror('Error', 'Incorrect Email ID')
          else:
                query= 'update datas set password=%s where email = %s'
                mycursor.execute(query, (password.get(),email.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Confirmation","New Password has been set")
                forget_window.destroy()
                import Login

def login_page():
      forget_window.destroy()
      import Login



# GUI
forget_window = Tk()
forget_window.title("Forget Password")
forget_window.geometry("1100x800")
forget_window.resizable(False,False)
#variables

password= StringVar()
email = StringVar()
cpassword = StringVar()

bgPic = ImageTk.PhotoImage(file='bag.png')

bglbl= Label(forget_window,image=bgPic)
bglbl.grid(row=0,column=0)

heading= Label(forget_window,text='RESET PASSWORD', font=('Microsoft Yahei UI Light',19,'bold underline'),bg="white",fg='firebrick1')
heading.place(x=693,y=130)

Email= Label(forget_window,text='Email', font=('Microsoft Yahei UI Light',15,'bold'),bg="white",fg='firebrick1')
Email.place(x=670,y=200)

EmailEntry= Entry(forget_window,width=25,font=('Microsoft Yahei UI, Light',16,'bold'),bd=0,fg='white',bg='firebrick1', textvariable=email)
EmailEntry.place(x=670,y=250)

Password= Label(forget_window,text='New Password', font=('Microsoft Yahei UI Light',15,'bold'),bg="white",fg='firebrick1')
Password.place(x=670,y=320)

PasswordEntry= Entry(forget_window,width=25,font=('Microsoft Yahei UI, Light',16,'bold'),bd=0,fg='white',bg='firebrick1', textvariable=password)
PasswordEntry.place(x=670,y=370)

ConfirmPassword= Label(forget_window,text='Confirm Password', font=('Microsoft Yahei UI Light',15,'bold'),bg="white",fg='firebrick1')
ConfirmPassword.place(x=670,y=440)

ConfirmPasswordEntry= Entry(forget_window,width=25,font=('Microsoft Yahei UI, Light',16,'bold'),bd=0,fg='white',bg='firebrick1', textvariable=cpassword)
ConfirmPasswordEntry.place(x=670,y=490)

Submitbtn = Button(forget_window,text='Confirm',font=('Open Sans',15,'bold'),fg='white',bg='firebrick1',activebackground='white',activeforeground='firebrick1',cursor='hand2',bd=0,width=15, command= change_password)
Submitbtn.place(x=725,y=550)

loggedin = Button(forget_window,text='Back to Log in',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',bd=0,width=21,command=login_page)
loggedin.place(x=745,y=600)




forget_window.mainloop()