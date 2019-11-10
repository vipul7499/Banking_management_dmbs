import tkinter as tk
import sqlite3
from sqlite3 import Error
import datetime
from datetime import date
def view_loan(cust_id):
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
    tk.Label(print_cust, text="LOAN NUMBER      ").grid(row=0 , column = 0)
    tk.Label(print_cust, text="LOAN AMOUNT      ").grid(row=0 , column = 1)
    tk.Label(print_cust, text="START DATE      ").grid(row=0 , column = 2)
    tk.Label(print_cust, text="END DATE      ").grid(row=0 , column = 3)
    tk.Label(print_cust, text="RATE      ").grid(row=0 , column = 4)
    tk.Label(print_cust, text="TYPE      ").grid(row=0 , column = 5)

    def printloan(loan_id , count):
        cursorObj.execute("SELECT * FROM LOAN where LOAN_NO = "+loan_id)    
        rows = cursorObj.fetchall()
        for i , row in enumerate(rows):
            tk.Label(print_cust, text=row[0]).grid(row=count , column = 0)
            tk.Label(print_cust, text=row[1]).grid(row=count , column = 1)
            tk.Label(print_cust, text=row[2]).grid(row=count , column = 2)
            tk.Label(print_cust, text=row[2]).grid(row=count , column = 3)
            tk.Label(print_cust, text=row[2]).grid(row=count , column = 4)
            tk.Label(print_cust, text=row[2]).grid(row=count , column = 5)
            
            
    count = 1
    cursorObj.execute("SELECT * FROM BORROWS where CUST_ID = "+cust_id)
    rows = cursorObj.fetchall()
    for row in rows:
        cursorObj.execute("SELECT count(*) FROM LOAN where LOAN_NO = "+row[0])
        no = cursorObj.fetchall()
        printloan(row[0] , count)
        count = count+1
    
    print_cust.mainloop()
    con.close()
#view_loan('100')
