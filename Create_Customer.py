import tkinter as tk
from tkinter import *
from datetime import date
import sqlite3
from sqlite3 import Error
import tkinter
import tkinter.messagebox

def sql_connection():
    try:
        con = sqlite3.connect('Banking_management.db')
        return con
    except Error:
        print(Error)

def create_customer():
    def show_entry_fields():
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("SELECT count(*) FROM CUSTOMER")    
        row1 = cursorObj.fetchall()
        cust_id = str(date.today())
        cust_id = ''.join(cust_id.split('-'))
        cust_id = cust_id+str(row1[0][0]) + '0'
        cursorObj.execute("INSERT INTO CUSTOMER"+ " (CUST_ID , PHONE_NUMBER , ADDRESS , FIRST_NAME , LAST_NAME , DATE_OF_BIRTH) VALUES(" + cust_id + ",'" + e5.get() + "','" + e4.get() + "','" + e1.get() + "','" + e2.get() + "','" + e3.get() + "')")
        con.commit()
        tkinter.messagebox.showinfo( "DONE" , "CUSTOMER ID is : " + cust_id)
        con.close()
        master.destroy()

    master = tk.Tk()
    tk.Label(master, text="First Name").grid(row=0)
    tk.Label(master, text="Last Name").grid(row=1)
    tk.Label(master, text="Date of birth(YYYY-MM-DD)").grid(row=2)
    tk.Label(master, text="Address").grid(row=3)
    tk.Label(master, text="Phone number").grid(row=4)


    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e5 = tk.Entry(master)


    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)

    tk.Button(master, 
              text='Confirm', command=show_entry_fields).grid(row=5, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)
    tk.mainloop()
