# from tkinter.ttk import Treeview
# from tkinter import *
# import tkinter as tk


# def on_double_click(event):
#     item_id = event.widget.focus()
#     item = event.widget.item(item_id)
#     print(item)
#     # values = item['values']
#     # url = values[0]
#     # print("the url is:", url)


# root= Tk()
# tree = Treeview()
# tree["columns"]=("one","two","three","four","five")
# tree.column("#0", width=1)
# tree.column("one", width=70)
# tree.column("two", width=80)
# tree.column("three", width=80)
# tree.column("four", width=80)
# tree.column("five", width=40)
# tree.heading("#0",text="ID")
# tree.heading("one", text="Name",anchor=W)
# tree.heading("two", text="Family",anchor=W)
# tree.heading("three", text="Code",anchor=W)
# tree.heading("four", text="B. Date",anchor=W)
# tree.heading("five", text="Class",anchor=W)
# tree.insert("", 1, text=1, values=(2,3,4, 5, 6))
# tree.grid(row=1, column=0, columnspan=4, sticky=W+E)
# tree.bind("<Double-Button-1>", on_double_click)

# root.mainloop()

# # from tkinter import *

# # root = Tk()

# # def callback(event):
# #     print( "clicked at", event.x, event.y)

# # frame = Frame(root, width=100, height=100)
# # frame.bind("<Button-1>", callback)
# # frame.pack()

# # root.mainloop()


a = {
    'text': 3,
    'image': '',
    'values': ['foad', 'khomami', 5646532125, '2002-08-14', 'Red'],
    'open': 0,
    'tags': ''
}
print(a['text'],a['values'][0] )