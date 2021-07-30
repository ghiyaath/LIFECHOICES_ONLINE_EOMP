from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkinter.ttk import Treeview
import pymysql
from tkinter import messagebox
import datetime as dt
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("Python: Simple Inventory System")
root.geometry("640x480")
root.bind('<Control-a>', lambda z: admins())

# Variables
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
NUMBER = StringVar()
IDNUMBER = StringVar()
EMAIL = StringVar()
NXTNAME = StringVar()
NXTNUMBER = StringVar()


def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)


def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=ToggleTonextRegister)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)


def nextRegisterForm():
    global nxtRegisterFrame, lbl_result2
    nxtRegisterFrame = Frame(root)
    nxtRegisterFrame.pack(side=TOP, pady=40)
    nxtRegisterFrame.place(height=530, width=640)
    lbl_number = Label(nxtRegisterFrame, text="PhoneNumber:", font=('arial', 18), bd=18)
    lbl_number.grid(row=1)
    lbl_IDnumber = Label(nxtRegisterFrame, text="IDNumber:", font=('arial', 18), bd=18)
    lbl_IDnumber.grid(row=2)
    lbl_email = Label(nxtRegisterFrame, text="Email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=3)
    lbl_nxtKinName = Label(nxtRegisterFrame, text="NextOfKinName:", font=('arial', 18), bd=18)
    lbl_nxtKinName.grid(row=4)
    lbl_nxtKinNumber = Label(nxtRegisterFrame, text="NextOfKinNumber:", font=('arial', 18), bd=18)
    lbl_nxtKinNumber.grid(row=5)
    lbl_result2 = Label(nxtRegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=6, columnspan=2)
    number = Entry(nxtRegisterFrame, font=('arial', 20), textvariable=NUMBER, width=15)
    number.grid(row=1, column=1)
    IDnumber = Entry(nxtRegisterFrame, font=('arial', 20), textvariable=IDNUMBER, width=15)
    IDnumber.grid(row=2, column=1)
    email = Entry(nxtRegisterFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=3, column=1)
    nxtKinName = Entry(nxtRegisterFrame, font=('arial', 20), textvariable=NXTNAME, width=15)
    nxtKinName.grid(row=4, column=1)
    nxtKinNumber = Entry(nxtRegisterFrame, font=('arial', 20), textvariable=NXTNUMBER, width=15)
    nxtKinNumber.grid(row=5, column=1)
    btn_login = Button(nxtRegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=7, columnspan=2, pady=20)
    btn_login.place(x=70, y=400)
    lbl_back = Label(nxtRegisterFrame, text="Back", fg="Blue", font=('arial', 12))
    lbl_back.grid(row=0, sticky=W)
    lbl_back.bind('<Button-1>', ToggleToBack)


def screen():
    global ScreenFrame
    ScreenFrame = Frame(root)
    ScreenFrame.place(height=530, width=640)
    lbl = Label(ScreenFrame, text="Welcome To LifeChoices Online", font=('Arial', 26, 'bold'))
    lbl.place(x=60, y=20)

    lbl4 = Label(ScreenFrame, text="Username:", font=('Arial', 20, 'bold'), fg='black')
    lbl4.place(x=90, y=150)
    lbl5 = Label(ScreenFrame, text=USERNAME.get(), font=('Arial', 20, 'bold'), fg='black')
    lbl5.place(x=300, y=150)

    lbl2 = Label(ScreenFrame, text='Login Time:', font=('Arial', 20, "bold"), fg='black')
    lbl2.place(x=90, y=200)
    lbl3 = Label(ScreenFrame, text=f"{dt.datetime.now():%a, %b %d %Y %H:%M:%S}", font=('Arial', 20, 'bold'),
                 fg='black')
    lbl3.place(x=300, y=200)
    btn2 = Button(ScreenFrame, text="LOGOUT", command=Logout, font=('arial', 18), width=35)
    btn2.place(x=80, y=400)


# Methods
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Logout():
    if messagebox.askyesno("confirm Log Out?", "Are you sure you want to Log Out?"):
        ScreenFrame.destroy()
        LoginForm()
        date = f"{dt.datetime.now():%a, %b %d %Y %H:%M:%S}"
        with open("User_Code.txt", 'a') as file:
            file.write('LogOut Date and Time: ' + date + '\n' + '\n')
    else:
        return True


def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()


def ToggleToBack(event=None):
    nxtRegisterFrame.destroy()
    RegisterForm()


def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()


def ToggleTonextRegister(event=None):
    RegisterFrame.destroy()
    nextRegisterForm()


def ToggleToScreen(event=None):
    LoginFrame.destroy()
    screen()


def Register():
    if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get() == "" or NUMBER.get() == "" or IDNUMBER.get() == "" or EMAIL.get() == "" or NXTNAME.get() == "" or NXTNUMBER.get() == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                              database='LIFECHOICES_ONLINE')
        cur = con.cursor()
        cur.execute("select * from Login where username=%s", USERNAME.get())
        row = cur.fetchone()
        if row != None:
            messagebox.showerror("Error", "Username already Exist, Please try with another Username", parent=root)
        else:
            # try:
            con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                  database='LIFECHOICES_ONLINE')
            cur = con.cursor()
            cur.execute(
                "insert into registration(name, surname, IDnumber, phoneNumber, email, nxtOfKinName, nxtOfKinNumber) values(%s, %s, %s, %s, %s, %s, %s)",
                (FIRSTNAME.get(), LASTNAME.get(), IDNUMBER.get(), NUMBER.get(), EMAIL.get(), NXTNAME.get(),
                 NXTNUMBER.get()))
            con.commit()
            cur1 = con.cursor()
            cur1.execute("insert into Login(username, password) values(%s, %s)", (USERNAME.get(), PASSWORD.get()))
            con.commit()
            lbl_result2.config(text="Successfully Created!", fg="black")
            ToggleToLogin()
            con.close()


def Login():
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                              database='LIFECHOICES_ONLINE')
        cur = con.cursor()
        cur.execute('select * from Login where username=%s and password=%s', (USERNAME.get(), PASSWORD.get()))
        row = cur.fetchone()
        if row == None:
            lbl_result1.config(text="Invalid Username or password", fg="red")
        else:
            ToggleToScreen()
            con.close()
            date = f"{dt.datetime.now():%a, %b %d %Y %H:%M:%S}"
            with open("User_Code.txt", 'a') as file:
                file.write('Username: ' + str(USERNAME.get()) + '\n')
                file.write('LogIn Date and Time: ' + date + '\n')


LoginForm()


def admins():
    root.destroy()
    import main1

# Menubar Widgets
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.mainloop()
