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