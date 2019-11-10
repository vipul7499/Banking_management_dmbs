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

def give_loan():
    def show_entry_fields():
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("SELECT count(*) FROM LOAN")    
        row1 = cursorObj.fetchall()
        count = row1[0][0]+1
        loan_no = str(date.today())
        loan_no = ''.join(loan_no.split('-'))
        loan_no = loan_no+str(count) + '1'
        if(count != 0):
            cursorObj.execute("INSERT INTO LOAN"+ " (LOAN_NO , LOAN_AMOUNT , START_DATE , END_DATE , RATE , TYPE) VALUES(" + loan_no + "," + e2.get() + ",'" + e3.get() + "','" + e4.get() +"',"+e5.get()+",'"+e6.get()+ "')")
            cursorObj.execute("INSERT INTO BORROWS"+ " (LOAN_NO , CUST_ID) VALUES(" + loan_no + "," + e1.get()+ ")")
            con.commit()
            tkinter.messagebox.showinfo( "DONE" , "LOAN ID is :"+loan_no )
            con.close()
            master.destroy()
        else:
            error5 = tk.Label(master, text="INVALID CUSTOMER ID" , bg = 'red')
            error5.grid(row=6)

            
    master = tk.Tk()
    tk.Label(master, text="Customer ID").grid(row=0)
    tk.Label(master, text="Amount").grid(row=1)
    tk.Label(master, text="Start Date(YYYY-MM-DD)").grid(row=2)
    tk.Label(master, text="End Date(YYYY-MM-DD)").grid(row=3)
    tk.Label(master, text="Rate").grid(row=4)
    tk.Label(master, text="Type").grid(row=5)


    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e5 = tk.Entry(master)
    e6 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)

    tk.Button(master, 
              text='Confirm', command=show_entry_fields).grid(row=7, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)
    tk.mainloop()
 
#give_loan()
