from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

window = Tk()
window.title("LifeChoices Online")
window.geometry("640x480")

username = StringVar()
password = StringVar()


def Admin():
    global Admin_frame, lbl_result3

    Admin_frame = Frame(window)
    Admin_frame.place(height=530, width=640)

    label1 = Label(Admin_frame, text="Admin Login", font=('Arial', 32, 'bold'), fg='black')
    label1.place(x=180, y=20)

    label2 = Label(Admin_frame, text='Username:', textvariable=username, font=('Arial', 20, 'bold'), fg='black')
    label2.place(x=30, y=145)
    user_name = Entry(Admin_frame, font=("Arial", 15, 'bold'))
    user_name.place(x=250, y=145, width=270, height=35)

    label3 = Label(Admin_frame, text="Password:", textvariable=password, font=("Arial", 20, 'bold'), fg="black")
    label3.place(x=30, y=195)
    PASSWORD = Entry(Admin_frame, font=("Arial", 15, 'bold'), show="*")
    PASSWORD.place(x=30, y=195, width=270, height=35)

    btn2 = Button(Admin_frame, text="Login", command=admin, font=('arial', 18), width=35)
    btn2.place(x=90, y=340)


# Admin login page, displays when clicking ctr+a
def adminLogin():
    # ADMIN USERNAME AND PASSWORD
    userName = "Admin"
    passWord = "Admin1234"
    try:
        if username.get() == userName and (password.get()) == passWord:
            Admin_frame.destroy()
            admin()
            return lbl_result3.config(text="Success, Click Ok to continue", fg="black")
        elif (username.get()) == "" and (password.get()) == "":
            lbl_result3.config(text="Invalid Username or password", fg="red")
        elif (username.get() != userName or password.get() != passWord):
            lbl_result3.config(text="Invalid Username or password", fg="red")
    except IndexError:
        messagebox.showerror("Error", "Please Enter a Valid Username and Password ")


def admin():
    window.destroy()
    import main1
Admin()

window.mainloop()
