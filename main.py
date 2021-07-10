from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import pymysql
import mysql.connector

root = Tk()
root.title("LIFECHOICES ONLINE")

width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.bind()

USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()


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
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=5, columnspan=2)
    name = Entry(RegisterFrame, font=('arial', 20), textvariable=NAME, width=15)
    name.grid(row=1, column=1)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=NAME, width=15)
    username.grid(row=2, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=4, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=5, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()


def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()


def Register():
    con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                          database='LIFECHOICES_ONLINE')
    cur = con.cursor()
    if USERNAME.get() == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get() == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        cur.execute("SELECT * FROM Register WHERE username=%s", (USERNAME.get(),))
        if cur.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cur.execute("INSERT INTO  (username, password, firstname, lastname) VALUES(%s, %s, %s, %s)",
                        (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
            con.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cur.close()
        con.close()


def Login():
    con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                          database='LIFECHOICES_ONLINE')
    cur = con.cursor()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cur.execute("SELECT * FROM Login WHERE username=%s and password=%s", (USERNAME.get(), PASSWORD.get()))
        if cur.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from tkinter.ttk import Treeview
from mysql.connector import cursor


def update(row):
    trv.delete(*trv.get_children())
    for i in row:
        trv.insert("", 'end', values=i)


def search():
    q2 = q.get()
    cur.execute("select * from Register where name like '%" + q2 + "%' or surname like '%" + q2 + "%'")
    row = cur.fetchall()
    update(row)


def clear():
    cur.execute("select * from Register")
    row = cur.fetchall()
    update(row)


def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])


def update_details():
    name = t1.get()
    surname = t2.get()
    ID = t3.get()
    phone = t4.get()
    nxtName = t5.get()
    nxtNumber = t6.get()
    if messagebox.askyesno("confirm Please?", "Are you sure you want to update?"):
        cur = con.cursor()
        query = "UPDATE Register SET name=%, surname=%, IDnumber=%, phoneNumber=%, nxtOfName=%, nxtOfNumber=% WHERE id=%;"
        cur.execute(query, (name, surname, ID, phone, nxtName, nxtNumber))
        con.commit()
        con.close()
        clear()
    else:
        return True


def add_new():
    name = t1.get()
    surname = t2.get()
    ID = t3.get()
    phone = t4.get()
    nxtName = t5.get()
    nxtNumber = t6.get()
    cur = con.cursor()
    query = "insert into Register value(name, surname, IDnumber, phoneNumber, nxtOfKinName, nxtOfKinNumber, date) VALUE(%s, %s, %s, %s, %s, %s, NOW())"
    cur.execute(query, (name, surname, ID, phone, nxtName, nxtNumber))
    con.commit()
    con.close()
    clear()


def delete_details():
    name = t1.get()
    if messagebox.askyesno("confirm Delete?", "Are you sure you want to delete this customer?"):
        cur = con.cursor()
        query = "DELETE FROM Register WHERE name= " + name
        cur.execute(query)
        con.commit()
        con.close()
        clear()
    else:
        return True


con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                      database='LifeChoices_Online')
cur = con.cursor()

window = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()

# Here I Created The Frames For Details,Search and Data
wrapper1 = LabelFrame(window, text="Details")
wrapper2 = LabelFrame(window, text="Search")
wrapper3 = LabelFrame(window, text="Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=20)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=20)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=20)

# Here Displays The Headings In Details
trv = ttk.Treeview(wrapper1, column=(1, 2, 3, 4, 5, 6), show="headings", height="6")
trv.pack()

trv.heading(1, text="Name")
trv.heading(2, text="Surname")
trv.heading(3, text="ID Number")
trv.heading(4, text="Phone Number")
trv.heading(5, text="Next Of Kin Name")
trv.heading(6, text="Next Of Kin Number")

trv.bind('<Double 1>', getrow)

cur.execute("select * from Register")
row = cur.fetchall()
update(row)

# The Search Labels and Entries
lbl = Label(wrapper2, text="Seacrh")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)
clear_btn = Button(wrapper2, text="Clear", command=clear)
clear_btn.pack(side=tk.LEFT, padx=6)

# The Users Data Labels and Entries
lbl1 = Label(wrapper3, text="Name")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="Surname")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="ID Number")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Phone Number")
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

lbl5 = Label(wrapper3, text="Next of Kin Name")
lbl5.grid(row=4, column=0, padx=5, pady=3)
ent5 = Entry(wrapper3, textvariable=t5)
ent5.grid(row=4, column=1, padx=5, pady=3)

lbl6 = Label(wrapper3, text="Next of Kin ")
lbl6.grid(row=5, column=0, padx=5, pady=3)
ent6 = Entry(wrapper3, textvariable=t6)
ent6.grid(row=5, column=1, padx=5, pady=3)

update_btn = Button(wrapper3, text="Update", command=update_details)
add_btn = Button(wrapper3, text="Add New", command=add_new)
delete_btn = Button(wrapper3, text="Delete", command=delete_details)

add_btn.grid(row=6, column=0, padx=5, pady=3)
update_btn.grid(row=6, column=1, padx=5, pady=3)
delete_btn.grid(row=6, column=2, padx=5, pady=3)

window.title("LifeChoices Online")
window.geometry("1000x700")
window.mainloop()

LoginForm()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()
