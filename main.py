import tkinter as tk
from tkinter import *

def reset():
    gentleman_ent.delete(0, END)
    glenfiddich_ent.delete(0, END)
    macallan_ent.delete(0, END)
    black_ent.delete(0, END)
    talisker_ent.delete(0, END)
    wild_ent.delete(0, END)
    glenmorangie_ent.delete(0, END)

def total():
    try: ent1=int(gentleman.get())
    except: ent1=0

    try: ent2=int(glenfiddich.get())
    except: ent2=0

    try: ent3=int(macallan.get())
    except: ent3=0

    try: ent4=int(black.get())
    except: ent4=0

    try: ent5=int(talisker.get())
    except: ent5=0

    try: ent6=int(wild.get())
    except: ent6=0

    try: ent7=int(glenmorangie.get())
    except: ent7=0

    # Defining cost
    cost1=ent1*20
    cost2=ent2*40
    cost3=ent3*85
    cost4=ent4*25
    cost5=ent5*110
    cost6=ent6*25
    cost7=ent7*30

    lbl_tot=Label(frame3, text='Total', font=('aria', 20, 'bold'), bg='black', fg='lightyellow', width=18)
    lbl_tot.place(x=0, y=50)

    ent_tot=Entry(frame3, textvariable=total_bill, font=('aria', 20, 'bold'), bg='lightgreen', bd=5, width=15, justify='center')
    ent_tot.place(x=35, y=100)

    total_cost=cost1+cost2+cost3+cost4+cost5+cost6+cost7
    string_bill=str(total_cost)+' PLN'
    total_bill.set(string_bill)

root=Tk()
root.geometry('1000x500+300+300')
root.title('Bill Management System')
root.resizable(False, False)

# Top part
Label(text='BILL MANAGEMENT SYSTEM', bg='black', fg='white', font=('Arial', 30, 'bold'), width=45, height=2).pack() # pack() places the label in a centre

# Menu
frame1=Frame(root, bg='lightgreen', highlightbackground='black', highlightthickness=1, width=300, height=370) # highlight works like border but thinner
frame1.place(x=10, y=118)

Label(frame1, text='MENU', font=('Gabriola', 40, 'bold'), bg='lightgreen', fg='black').place(x=80, y=0)
Label(frame1, text='Gentleman Jack.........20 PLN', font=('Lucida Calligraphy', 12, 'bold'), bg='lightgreen', fg='black').place(x=10, y=80)
Label(frame1, text='Glenfiddich 12yo........40 PLN', font=('Lucida Calligraphy', 12, 'bold'), bg='lightgreen', fg='black').place(x=10, y=110)
Label(frame1, text='Macallan 12yo...........85 PLN', font=('Lucida Calligraphy', 12, 'bold'), bg='lightgreen', fg='black').place(x=10, y=140)
Label(frame1, text='Black Label................25 PLN', font=('Lucida Calligraphy', 12, 'bold'), bg='lightgreen', fg='black').place(x=10, y=170)
Label(frame1, text='Talisker 30yo............110 PLN', font=('Lucida Calligraphy', 12, 'bold'), bg='lightgreen', fg='black').place(x=10, y=200)
Label(frame1, text='Wild Turkey..............25 PLN', font=('Lucida Calligraphy', 12, 'bold'), bg='lightgreen', fg='black').place(x=10, y=230)
Label(frame1, text='Glenmorangie 12yo....30 PLN', font=('Lucida Calligraphy', 12, 'bold'), bg='lightgreen', fg='black').place(x=10, y=260)

# Entry work
frame2=Frame(root, bd=5, width=300, height=370, relief=RAISED) # bd - borderwidth, relief - border style
frame2.place(x=330, y=125)

gentleman=StringVar()
glenfiddich=StringVar()
macallan=StringVar()
black=StringVar()
talisker=StringVar()
wild=StringVar()
glenmorangie=StringVar()

# Label of entry
gentleman_lbl=Label(frame2, text='Gentleman Jack', font=('Aria', 18, 'bold'), fg='blue4', width=12)
glenfiddich_lbl=Label(frame2, text='Glenfiddich', font=('Aria', 18, 'bold'), fg='blue4', width=12)
macallan_lbl=Label(frame2, text='Macallan', font=('Aria', 18, 'bold'), fg='blue4', width=12)
black_lbl=Label(frame2, text='Black Label', font=('Aria', 18, 'bold'), fg='blue4', width=12)
talisker_lbl=Label(frame2, text='Talisker', font=('Aria', 18, 'bold'), fg='blue4', width=12)
wild_lbl=Label(frame2, text='Wild Turkey', font=('Aria', 18, 'bold'), fg='blue4', width=12)
glenmorangie_lbl=Label(frame2, text='Glenmorangie', font=('Aria', 18, 'bold'), fg='blue4', width=12)

gentleman_lbl.grid(row=1, column=0)
glenfiddich_lbl.grid(row=2, column=0)
macallan_lbl.grid(row=3, column=0)
black_lbl.grid(row=4, column=0)
talisker_lbl.grid(row=5, column=0)
wild_lbl.grid(row=6, column=0)
glenmorangie_lbl.grid(row=7, column=0)

# Entry
gentleman_ent=Entry(frame2, textvariable=gentleman, font=('Aria', 18, 'bold'), bg='lightpink', bd=6, width=8, justify='center')
glenfiddich_ent=Entry(frame2, textvariable=glenfiddich, font=('Aria', 18, 'bold'), bg='lightpink', bd=6, width=8, justify='center')
macallan_ent=Entry(frame2, textvariable=macallan, font=('Aria', 18, 'bold'), bg='lightpink', bd=6, width=8, justify='center')
black_ent=Entry(frame2, textvariable=black, font=('Aria', 18, 'bold'), bg='lightpink', bd=6, width=8, justify='center')
talisker_ent=Entry(frame2, textvariable=talisker, font=('Aria', 18, 'bold'), bg='lightpink', bd=6, width=8, justify='center')
wild_ent=Entry(frame2, textvariable=wild, font=('Aria', 18, 'bold'), bg='lightpink', bd=6, width=8, justify='center')
glenmorangie_ent=Entry(frame2, textvariable=glenmorangie, font=('Aria', 18, 'bold'), bg='lightpink', bd=6, width=8, justify='center')

gentleman_ent.grid(row=1, column=1)
glenfiddich_ent.grid(row=2, column=1)
macallan_ent.grid(row=3, column=1)
black_ent.grid(row=4, column=1)
talisker_ent.grid(row=5, column=1)
wild_ent.grid(row=6, column=1)
glenmorangie_ent.grid(row=7, column=1)

reset_btn=Button(frame2, text='Reset', font=('ariel', 16, 'bold'), bg='lightblue', fg='black', bd=5, width=10, command=reset)
total_btn=Button(frame2, text='Total', font=('ariel', 16, 'bold'), bg='lightblue', fg='black', bd=5, width=10, command=total)

reset_btn.grid(row=8, column=0)
total_btn.grid(row=8, column=1)

# Bill
frame3=Frame(root, bg='lightyellow', highlightbackground='black', highlightthickness=1, width=300, height=370)
frame3.place(x=690, y=118)

bill=Label(frame3, text='Bill', font=('Calibri', 20, 'bold'), bg='lightyellow')
bill.place(x=133, y=10)

total_bill=StringVar()

root.mainloop()