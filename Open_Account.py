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

def open_account():
    def show_entry_fields():
        def sav_acc():
            con = sql_connection()
            cursorObj = con.cursor()
            cursorObj.execute("SELECT count(*) FROM CUSTOMER where CUST_ID = "+e1.get())
            row =cursorObj.fetchall()
            if(row[0][0] != 0):
                cursorObj.execute("SELECT count(*) FROM SAVINGS_ACCOUNT")    
                row1 = cursorObj.fetchall()
                account_id = str(date.today())
                account_id = ''.join(account_id.split('-'))
                account_id = account_id+str(row1[0][0]) + '2'
                cursorObj.execute("INSERT INTO SAVINGS_ACCOUNT(ACCOUNT_ID , INTEREST_RATE , BALANCE) VALUES ("+account_id+" , "+e3.get()+","+e2.get()+" )")
                cursorObj.execute("INSERT INTO DEPOSITS(ACCOUNT_ID , CUST_ID) VALUES ("+account_id+" , "+e1.get()+" )")
                con.commit()
                tkinter.messagebox.showinfo( "DONE" , "ACCOUNT ID is : " + account_id)
                con.close()
                master.destroy()
            else:
                error5 = tk.Label(master, text="INVALID CUSTOMER ID" , bg = 'red')
                error5.grid(row=3)
        #row1 = cursorObj.fetchall()
            #print("hi")
        def curr_acc():
            con = sql_connection()
            cursorObj = con.cursor()
            cursorObj.execute("SELECT count(*) FROM CUSTOMER where CUST_ID = "+e1.get())
            row =cursorObj.fetchall()
            if(row[0][0] != 0):
                cursorObj.execute("SELECT count(*) FROM CURRENT_ACCOUNT")    
                row1 = cursorObj.fetchall()
                account_id = str(date.today())
                account_id = ''.join(account_id.split('-'))
                account_id = account_id+str(row1[0][0]) + '2'
                cursorObj.execute("INSERT INTO CURRENT_ACCOUNT(ACCOUNT_ID , OVERDRAFT_AMOUNT , BALANCE) VALUES ("+account_id+" , "+e3.get()+","+e2.get()+" )")
                cursorObj.execute("INSERT INTO DEPOSITS(ACCOUNT_ID , CUST_ID) VALUES ("+account_id+" , "+e1.get()+" )")
                con.commit()
                tkinter.messagebox.showinfo( "DONE" , "ACCOUNT ID is : " + account_id)
                con.close()
                master.destroy()
            else:
                error5 = tk.Label(master, text="INVALID CUSTOMER ID" , bg = 'red')
                error5.grid(row=3)
        if(Account_type.get() == "SAVINGS_ACCOUNT"):
            option.destroy()
            tk.Label(master, text="Customer ID").grid(row=0)
            tk.Label(master, text="Balance").grid(row=1)
            tk.Label(master, text="Interest Rate").grid(row=2)
            
            e1 = tk.Entry(master)
            e2 = tk.Entry(master)
            e3 = tk.Entry(master)
            
            e1.grid(row=0, column=1)
            e2.grid(row=1, column=1)
            e3.grid(row=2, column=1)
            
            tk.Button(master, 
              text='Confirm', command=sav_acc).grid(row=5, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)
        else:
            option.destroy()
            tk.Label(master, text="Customer ID").grid(row=0)
            tk.Label(master, text="Balance").grid(row=1)
            tk.Label(master, text="Overdraft Amount").grid(row=2)        

            e1 = tk.Entry(master)
            e2 = tk.Entry(master)
            e3 = tk.Entry(master)

            e1.grid(row=0, column=1)
            e2.grid(row=1, column=1)
            e3.grid(row=2, column=1)
            tk.Button(master, 
              text='Confirm', command=curr_acc).grid(row=5, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)
    master = tk.Tk()

    Account_type = StringVar(master)
    Account_type.set("SAVINGS_ACCOUNT") 

    option = OptionMenu(master, Account_type, "SAVINGS_ACCOUNT", "CURRENT_ACCOUNT")
    option.grid(row = 1,column = 0)


    tk.Button(master, 
              text='Confirm', command=show_entry_fields).grid(row=5, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)
    tk.mainloop()
#open_account()
