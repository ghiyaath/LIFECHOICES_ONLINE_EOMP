from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime as dt
import pymysql

window = Tk()
window.title("LifeChoices Online")
window.geometry("1200x700")


# logout function
def logOut():
    if messagebox.askyesno("confirm Log Out?", "Are you sure you want to Log Out?"):
        window.destroy()
        import main
        date = f"{dt.datetime.now():%a, %b %d %Y %H:%M:%S}"
        with open("User_Code.txt", 'a') as file:
            file.write('LogOut Date and Time: ' + date + '\n' + '\n')
    else:
        return True


# Admin page
def admin():
    admin_frame = Frame(window, bg='white')
    admin_frame.place(height=700, width=1000)


def update(row):
    trv.delete(*trv.get_children())
    for i in row:
        trv.insert("", 'end', values=i)


# This function gets the item that is searcher for
def search():
    con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                          database='LIFECHOICES_ONLINE')
    cur = con.cursor()
    q2 = q.get()
    cur.execute(
        "select id, name, surname, IDnumber, phoneNumber, email, nxtOfKinName, nxtOfKinNumber from registration where name like '%" + q2 + "%' or surname like '%" + q2 + "%' or IDnumber like '%" + q2 + "%' or phoneNumber like '%" + q2 + "%' or email like '%" + q2 + "%' or nxtOfKinName like '%" + q2 + "%' or nxtOfKinNumber like '%" + q2 + "%'")
    row = cur.fetchall()
    update(row)


# This function clears the in info in the search bar
def clear():
    con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                          database='LIFECHOICES_ONLINE')
    cur = con.cursor()
    cur.execute(
        "select id, name, surname, IDnumber, phoneNumber, email, nxtOfKinName, nxtOfKinNumber from registration")
    row = cur.fetchall()
    update(row)


# This function allows admin to display the users details in the Data when double clicking on it in Details
def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])
    t7.set(item['values'][6])
    t8.set(item['values'][7])


# Function that allows admin to make changes to the user
def update_details():
    User_id = t1.get()
    name = t2.get()
    surname = t3.get()
    ID = t4.get()
    phone = t5.get()
    email = t6.get()
    nxtName = t7.get()
    nxtNumber = t8.get()
    if messagebox.askyesno("confirm Please?", "Are you sure you want to update?"):
        con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                              database='LIFECHOICES_ONLINE')
        cur = con.cursor()
        query = "UPDATE registration SET name=%s, surname=%s, IDnumber=%s, phoneNumber=%s, email=%s, nxtOfKinName=%s, nxtOfKinNumber=%s WHERE id=%s"
        cur.execute(query, (name, surname, ID, phone, email, nxtName, nxtNumber, User_id))
        con.commit()
        con.close()
        clear()
    else:
        return True


# Function that creates new user
def add_new():
    name = t2.get()
    surname = t3.get()
    ID = t4.get()
    phone = t5.get()
    email = t6.get()
    nxtName = t7.get()
    nxtNumber = t8.get()
    con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                          database='LIFECHOICES_ONLINE')
    cur = con.cursor()
    cur.execute(
        "insert into registration(name, surname, IDnumber, phoneNumber, email, nxtOfKinName, nxtOfKinNumber) values(%s, %s, %s, %s, %s, %s, %s)",
        (name, surname, ID, phone, email, nxtName, nxtNumber))
    con.commit()
    con.close()

    # Delete function


def delete_details():
    User_id = t1.get()
    if messagebox.askyesno("confirm Delete?", "Are you sure you want to delete this customer?"):
        con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                              database='LIFECHOICES_ONLINE')
        cur = con.cursor()
        query = "DELETE FROM registration WHERE id=%s" % (User_id)
        cur.execute(query)
        con.commit()
        con.close()
        clear()
    else:
        return True


q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()

# Creates The Frames For Details, Search and Data
wrapper1 = LabelFrame(text="Details")
wrapper2 = LabelFrame(text="Search")
wrapper3 = LabelFrame(text="Data")

wrapper1.place(x=25, y=10, width=1100, height=200)
wrapper2.place(x=25, y=225, width=1100, height=150)
wrapper3.place(x=25, y=390, width=1100, height=300)

# Displays The Headings In Details
trv = ttk.Treeview(wrapper1, column=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="7")
trv.pack(side=tk.LEFT)
trv.place(x=0, y=0)
trv.heading(1, text="User_id")
trv.heading(2, text="Name")
trv.heading(3, text="Surname")
trv.heading(4, text="ID Number")
trv.heading(5, text="Phone Number")
trv.heading(6, text="Email")
trv.heading(7, text="Next Of Kin Name")
trv.heading(8, text="Next Of Kin Number")
trv.column(1, width=50, minwidth=100)
trv.column(2, width=150, minwidth=200)
trv.column(3, width=150, minwidth=200)
trv.column(4, width=150, minwidth=200)
trv.column(5, width=150, minwidth=200)
trv.column(6, width=150, minwidth=200)
trv.column(7, width=150, minwidth=200)
trv.column(8, width=150, minwidth=200)

trv.bind('<Double 1>', getrow)

# Vertical Scrollbar
yScrollBar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
yScrollBar.place(x=1080, y=0, height=160)

# Horizontal Scrollbar
xScrollBar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
xScrollBar.place(x=0, y=163, width=1090)
trv.configure(yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

# Displaying the details in Details
con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                      database='LIFECHOICES_ONLINE')
cur = con.cursor()
cur.execute("select * from registration")
row = cur.fetchall()
update(row)

# Search Labels and Entries
lbl = Label(wrapper2, text="Seacrh")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)
clear_btn = Button(wrapper2, text="Clear", command=clear)
clear_btn.pack(side=tk.LEFT, padx=6)

# User Data Labels and Entries
lbl1 = Label(wrapper3, text="User_id")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="Name")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="Surname")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="ID Number")
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

lbl5 = Label(wrapper3, text="Phone Number")
lbl5.grid(row=4, column=0, padx=5, pady=3)
ent5 = Entry(wrapper3, textvariable=t5)
ent5.grid(row=4, column=1, padx=5, pady=3)

lbl6 = Label(wrapper3, text="Email")
lbl6.grid(row=5, column=0, padx=5, pady=3)
ent6 = Entry(wrapper3, textvariable=t6)
ent6.grid(row=5, column=1, padx=5, pady=3)

lbl7 = Label(wrapper3, text="Next of Kin Name")
lbl7.grid(row=6, column=0, padx=5, pady=3)
ent7 = Entry(wrapper3, textvariable=t7)
ent7.grid(row=6, column=1, padx=5, pady=3)

lbl8 = Label(wrapper3, text="Next of Kin ")
lbl8.grid(row=7, column=0, padx=5, pady=3)
ent8 = Entry(wrapper3, textvariable=t8)
ent8.grid(row=7, column=1, padx=5, pady=3)

# Buttons
update_btn = Button(wrapper3, text="Update", command=update_details)
add_btn = Button(wrapper3, text="Add New", command=add_new)
delete_btn = Button(wrapper3, text="Delete", command=delete_details)
logout_btn = Button(wrapper3, text="LOGOUT", command=logOut)

add_btn.grid(row=8, column=0, padx=5, pady=3)
update_btn.grid(row=8, column=1, padx=5, pady=3)
delete_btn.grid(row=8, column=2, padx=5, pady=3)
logout_btn.place(x=850, y=205)

window.mainloop()
