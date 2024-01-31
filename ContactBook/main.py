#modules tkinter

#Here we can save, update, delete, view, search the contact details of individuals..

from tkinter import *
from tkinter import ttk
from view import *

#colors
co1 = "#ffffff" #white
co2 = "#000000" #black
co3 = "#4456F0" #blue

root = Tk()
root.geometry("485x450")
root.config(bg = co1)
root.resizable(width=False, height=False)
root.title("Contact Book")

#creating frames
frame_up = Frame(root, width=500, height=50, bg=co3)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(root, width=500, height=150, bg=co1)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(root, width=500, height=100, bg=co1, relief="flat")
frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

#functions
def show():
    global tree


    demo_list=[['sakthi','88258','sakthi@mail', 'bangalore']]


    list_header=['Name','Phone','Mail','Address']

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=tree.yview)

    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree head
    tree.heading(0, text='Nmae', anchor=NW)
    tree.heading(1, text='Phone', anchor=NW)
    tree.heading(2, text='Mail', anchor=NW)
    tree.heading(3, text='Address', anchor=NW)

    #tree columns
    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=50, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(3, width=180, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)


show()


#frame_up widgets
app_name = Label(frame_up, text="ContactBook", height=1, font=('verdana 17 bold'), bg=co3, fg= co1).place(x=5, y=5)

#frame_down widgets
#name
l_name= Label(frame_down, text="Name *", width=7, height=1, font=("Ivy 10"), bg=co1, anchor=NW).place(x=10, y=20)
e_name= Entry(frame_down, width=27, justify='left', highlightthickness=1, relief="solid").place(x=80, y= 20)

#phone number
l_phn= Label(frame_down, text="Phone *", width=7, height=1, font=("Ivy 10"), bg=co1, anchor=NW).place(x=10, y=50)
e_phn= Entry(frame_down, width=27, justify='left', highlightthickness=1, relief="solid").place(x=80, y= 50)

#email
l_mail= Label(frame_down, text="Mail *", height=1, font=("Ivy 10"), bg=co1, anchor=NW).place(x=10, y=80)
e_mail= Entry(frame_down, width=27, justify='left', highlightthickness=1, relief="solid").place(x=80, y=80)

#Address
l_addr= Label(frame_down, text="Address *", width=7, height=1, font=("Ivy 10"), bg=co1, anchor=NW).place(x=10, y=110)
e_addr= Entry(frame_down, width=27, justify='left', highlightthickness=1, relief="solid").place(x=80, y= 110)

#Creating Buttons
#search
b_search = Button(frame_down, text="Search", height=1, bg=co3, fg=co1, font=('Ivy 8 bold')).place(x=290, y=20)
e_search = Entry(frame_down, width=16, justify='left', font=('Ivy 11 '), highlightthickness=1, relief="solid").place(x=347, y= 20)

#view
b_view = Button(frame_down, text="View", width=10, height=1, bg=co3, fg=co1, font=('Ivy 8 bold')).place(x=290, y=50)

#add
b_add = Button(frame_down, text="Add", width=10, height=1, bg=co3, fg=co1, font=('Ivy 8 bold')).place(x=400, y=50)

#update
b_update = Button(frame_down, text="Update",width=10, height=1, bg=co3, fg=co1, font=('Ivy 8 bold')).place(x=400, y=80)

#delete
b_delete = Button(frame_down, text="Delete", width=10, height=1, bg=co3, fg=co1, font=('Ivy 8 bold')).place(x=400, y=110)

root.mainloop()