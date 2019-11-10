import tkinter as tk
from tkinter import *
from datetime import date
import sqlite3
from sqlite3 import Error
import tkinter
import tkinter.messagebox
import datetime

def sql_connection():
    try:
        con = sqlite3.connect('Banking_management.db')
        return con
    except Error:
        print(Error)

def create_fd():
    def show_entry_fields():
        con = sql_connection()
        cursorObj = con.cursor()
        ac_id = e1.get()
        cursorObj.execute("SELECT count(*) FROM SAVINGS_ACCOUNT where ACCOUNT_ID = "+ac_id)    
        row1 = cursorObj.fetchall()
        count = row1[0][0]
        cursorObj.execute("SELECT count(*) FROM CURRENT_ACCOUNT where ACCOUNT_ID = "+ac_id)    
        row1 = cursorObj.fetchall()
        count = count + row1[0][0]
        date = str(datetime.date.today() + datetime.timedelta( days = 365*int(e4.get()) ))
        
        if(count != 0):
            
            cursorObj.execute("INSERT INTO FIXED_DEPOSIT"+ " (ACCOUNT_ID , INTEREST , AMOUNT , TENURE) VALUES(" + ac_id + "," + e2.get() + "," + e3.get() + ",'" + date + "')")
            con.commit()
            tkinter.messagebox.showinfo( "DONE" , "FD HAS BEEN CREATED " )
            con.close()
            master.destroy()
        else:
            error5 = tk.Label(master, text="INVALID ACCOUNT ID" , bg = 'red')
            error5.grid(row=4)

            
    master = tk.Tk()
    tk.Label(master, text="Account ID").grid(row=0)
    tk.Label(master, text="Amount").grid(row=1)
    tk.Label(master, text="Interest").grid(row=2)
    tk.Label(master, text="Tenure(years)").grid(row=3)


    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)


    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)

    tk.Button(master, 
              text='Confirm', command=show_entry_fields).grid(row=5, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)
    tk.mainloop()
 
#create_fd()
