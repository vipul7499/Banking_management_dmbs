import tkinter as tk
import sqlite3
from sqlite3 import Error

def view_all_account(cust_id):
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
    tk.Label(print_cust, text="ID      ").grid(row=0 , column = 0)
    tk.Label(print_cust, text="BALANCE      ").grid(row=0 , column = 1)
    tk.Label(print_cust, text="INTEREST RATE      ").grid(row=0 , column = 2)
    tk.Label(print_cust, text="OVERDRAFT AMOUNT      ").grid(row=0 , column = 3)
    tk.Label(print_cust, text="TYPE      ").grid(row=0 , column = 4)

    def saving(account_id , count):
        cursorObj.execute("SELECT * FROM SAVINGS_ACCOUNT where ACCOUNT_ID = "+account_id)    
        rows = cursorObj.fetchall()
        for i , row in enumerate(rows):
            tk.Label(print_cust, text=row[0]).grid(row=count , column = 0)
            tk.Label(print_cust, text=row[1]).grid(row=count , column = 1)
            tk.Label(print_cust, text=row[2]).grid(row=count , column = 2)
            tk.Label(print_cust, text="-").grid(row=count , column = 3)
            tk.Label(print_cust, text="Savings Account").grid(row=count , column = 4)
    def curr(account_id , count):
        cursorObj.execute("SELECT * FROM CURRENT_ACCOUNT where ACCOUNT_ID = "+account_id)    
        rows = cursorObj.fetchall()
        for i , row in enumerate(rows):
            tk.Label(print_cust, text=row[0]).grid(row=count , column = 0)
            tk.Label(print_cust, text=row[1]).grid(row=count , column = 1)
            tk.Label(print_cust, text="-").grid(row=count , column = 2)
            tk.Label(print_cust, text=row[2]).grid(row=count , column = 3)
            tk.Label(print_cust, text="Current Account").grid(row=count , column = 4)
            

    count = 1
    cursorObj.execute("SELECT * FROM DEPOSITS where CUST_ID = "+cust_id)
    rows = cursorObj.fetchall()
    for row in rows:
        cursorObj.execute("SELECT count(*) FROM CURRENT_ACCOUNT where ACCOUNT_ID = "+row[0])
        no = cursorObj.fetchall()
        if(no[0][0] != 0):
            curr(row[0] , count)
        else:
            saving(row[0],count)
        count = count+1
    
    print_cust.mainloop()
    con.close()
#view_all_account('100')
