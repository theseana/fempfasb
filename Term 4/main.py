from tkcalendar import DateEntry

from tkinter import *
from tkinter.ttk import Notebook, Treeview
import datetime

import database


def to_year(date):
    m, d, y = date.split('/')
    return '20{}-{}-{}'.format(y.zfill(2), m.zfill(2), d.zfill(2))


def student_insert():
    database.StudentInsert(
        name.get(),
        family.get(),
        idN.get(),
        to_year(birth.get()),
        color.get()
    )
    name.set('')
    family.set('')
    idN.set('')
    birth.set('')
    color.set('')

def search_student():
    data = database.StudentSelect(name_student.get())
    names = data.get()
    tree = Treeview(s_select)
    tree["columns"]=("one","two","three","four","five")
    tree.column("#0", width=1)
    tree.column("one", width=70)
    tree.column("two", width=80)
    tree.column("three", width=80)
    tree.column("four", width=80)
    tree.column("five", width=40)
    tree.heading("#0",text="ID")
    tree.heading("one", text="Name",anchor=W)
    tree.heading("two", text="Family",anchor=W)
    tree.heading("three", text="Code",anchor=W)
    tree.heading("four", text="B. Date",anchor=W)
    tree.heading("five", text="Class",anchor=W)
    for name in names:
        tree.insert("", 1, text=name[0], values=(name[1],name[2],name[3], name[4], name[5]))
    tree.grid(row=1, column=0, columnspan=4, sticky=W+E)
root = Tk()

date = datetime.datetime.now()

note = Notebook()
note.grid(row=0, column=0)

s_insert = Frame()
s_update = Frame()
s_delete = Frame()
s_select = Frame()

note.add(s_insert, text='Student Insert')
note.add(s_select, text='Student Search')
note.add(s_update, text='Student Update')
note.add(s_delete, text='Student Delete')


# ######################################### #
Label(s_insert, text="Name").grid(row=0, column=0)
name = StringVar()
Entry(s_insert, textvariable=name).grid(row=0, column=1)

Label(s_insert, text="Family").grid(row=1, column=0)
family = StringVar()
Entry(s_insert, textvariable=family).grid(row=1, column=1)

Label(s_insert, text="ID N.").grid(row=2, column=0)
idN = StringVar()
Entry(s_insert, textvariable=idN).grid(row=2, column=1)

Label(s_insert, text="B. Date").grid(row=3, column=0)
birth = StringVar()
DateEntry(s_insert, textvariable=birth, year=date.year, month=date.month, 
          day=date.day).grid(row=3, column=1, sticky=W+E)

Label(s_insert, text="C. Color").grid(row=4, column=0)
color = StringVar()
color.set('Red')
OptionMenu(s_insert, color, 'Yellow', 'Red', 'Green', 'Orange').grid(row=4, column=1, sticky=W+E)

Button(s_insert, text='Create', command=student_insert).grid(row=5, column=0, columnspan=2, sticky=W+E)
Button(s_insert, text='Cancel', command=root.destroy).grid(row=6, column=0, columnspan=2, sticky=W+E)
# ######################################### #
Label(s_select, text="Name").grid(row=0,column=0)
name_student=StringVar()
Entry(s_select,textvariable=name_student).grid(row=0, column=1)
Button(s_select, text="Search", command=search_student).grid(row=0,column=2)



root.mainloop()
