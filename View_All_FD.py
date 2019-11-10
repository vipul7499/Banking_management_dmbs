import tkinter as tk
import sqlite3
from sqlite3 import Error
import datetime
from datetime import date
def view_fd(cust_id):
    def sql_connection():
        try:
            con = sqlite3.connect('Banking_management.db')
            return con
        except Error:
            print(Error)
    con = sql_connection()
    cursorObj = con.cursor()        
    count=  0
    print_cust = tk.Tk()
    tk.Label(print_cust, text="ACCOUNT ID      ").grid(row=0 , column = 0)
    tk.Label(print_cust, text="INTEREST      ").grid(row=0 , column = 1)
    tk.Label(print_cust, text="AMOUNT      ").grid(row=0 , column = 2)
    tk.Label(print_cust, text="TENURE(days)      ").grid(row=0 , column = 3)

    def printfd(account_id , count):
        cursorObj.execute("SELECT * FROM FIXED_DEPOSIT where ACCOUNT_ID = "+account_id)    
        rows = cursorObj.fetchall()
        for i , row in enumerate(rows):
            date_object = datetime.datetime.strptime(row[3], '%Y-%m-%d').date()
            day = date_object - date.today()
            day = day.days
            tk.Label(print_cust, text=row[0]).grid(row=count , column = 0)
            tk.Label(print_cust, text=row[1]).grid(row=count , column = 1)
            tk.Label(print_cust, text=row[2]).grid(row=count , column = 2)
            tk.Label(print_cust, text=day).grid(row=count , column = 3)
            
    count = 1
    cursorObj.execute("SELECT * FROM DEPOSITS where CUST_ID = "+cust_id)
    rows = cursorObj.fetchall()
    for row in rows:
        cursorObj.execute("SELECT count(*) FROM CURRENT_ACCOUNT where ACCOUNT_ID = "+row[0])
        no = cursorObj.fetchall()
        printfd(row[0] , count)
        count = count+1
    
    print_cust.mainloop()
    con.close()
#view_all_account('100')
