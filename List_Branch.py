import tkinter as tk
import sqlite3
from sqlite3 import Error

def print_branch():
    def sql_connection():
        try:
            con = sqlite3.connect('Banking_management.db')
            return con
        except Error:
            print(Error)
            
    print_cust = tk.Tk()
    tk.Label(print_cust, text="Branch ID      ").grid(row=0 , column = 0)
    tk.Label(print_cust, text="Branch Name      ").grid(row=0 , column = 1)
    tk.Label(print_cust, text="Branch City      ").grid(row=0 , column = 2)

    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM BRANCH")    
    rows = cursorObj.fetchall()
    for i , row in enumerate(rows):
        tk.Label(print_cust, text=row[0]).grid(row=i+1 , column = 0)
        tk.Label(print_cust, text=row[1]).grid(row=i+1 , column = 1)
        tk.Label(print_cust, text=row[2]).grid(row=i+1 , column = 2)

    print_cust.mainloop()
    con.close()
#print_customer()
