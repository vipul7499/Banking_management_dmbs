import tkinter as tk
import sqlite3
from sqlite3 import Error

def print_customer():
    def sql_connection():
        try:
            con = sqlite3.connect('Banking_management.db')
            return con
        except Error:
            print(Error)
            
    print_cust = tk.Tk()
    tk.Label(print_cust, text="Customer ID      ").grid(row=0 , column = 0)
    tk.Label(print_cust, text="First Name      ").grid(row=0 , column = 1)
    tk.Label(print_cust, text="Last Name      ").grid(row=0 , column = 2)
    tk.Label(print_cust, text="Date of birth(YYYY-MM-DD)      ").grid(row=0 , column = 3)
    tk.Label(print_cust, text="Address      ").grid(row=0, column = 4)
    tk.Label(print_cust, text="Phone number      ").grid(row=0 , column = 5)


    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM CUSTOMER")    
    rows = cursorObj.fetchall()
    for i , row in enumerate(rows):
        tk.Label(print_cust, text=row[0]).grid(row=i+1 , column = 0)
        tk.Label(print_cust, text=row[3]).grid(row=i+1 , column = 1)
        tk.Label(print_cust, text=row[4]).grid(row=i+1 , column = 2)
        tk.Label(print_cust, text=row[5]).grid(row=i+1 , column = 3)
        tk.Label(print_cust, text=row[2]).grid(row=i+1 , column = 4)
        tk.Label(print_cust, text=row[1]).grid(row=i+1 , column = 5)

    print_cust.mainloop()
    con.close()
