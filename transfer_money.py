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

def transfer_money(cust_id):
    def show_entry_fields():
        acc_no = e1.get()
        rec_acc_no = e2.get()
        amount = e3.get()
        if(int(amount) >= 0):
            con = sql_connection()
            cursorObj = con.cursor()
            cursorObj.execute("SELECT count(*) FROM SAVINGS_ACCOUNT where ACCOUNT_ID = "+acc_no)    
            row1 = cursorObj.fetchall()
            count = row1[0][0]
            cursorObj.execute("SELECT count(*) FROM CURRENT_ACCOUNT where ACCOUNT_ID = "+acc_no)    
            row1 = cursorObj.fetchall()
            count1 = row1[0][0]
            if( count + count1 >= 1):
                cursorObj.execute("SELECT count(*) FROM DEPOSITS where ACCOUNT_ID = "+acc_no + " and CUST_ID = "+cust_id)    
                row1 = cursorObj.fetchall()
                cust = row1[0][0]
                if(cust >= 1):
                    cursorObj.execute("SELECT count(*) FROM SAVINGS_ACCOUNT where ACCOUNT_ID = "+rec_acc_no)    
                    row1 = cursorObj.fetchall()
                    count2 = row1[0][0]
                    cursorObj.execute("SELECT count(*) FROM CURRENT_ACCOUNT where ACCOUNT_ID = "+rec_acc_no)    
                    row1 = cursorObj.fetchall()
                    count3 = row1[0][0]
                    if(count2 + count3 >= 1):
                        if(count == 1):
                            cursorObj.execute("SELECT balance FROM SAVINGS_ACCOUNT where ACCOUNT_ID = "+acc_no)
                            row = cursorObj.fetchall()
                            bal = row[0][0]
                        if(count1 == 1):
                            cursorObj.execute("SELECT balance FROM CURRENT_ACCOUNT where ACCOUNT_ID = "+acc_no)
                            row = cursorObj.fetchall()
                            bal = row[0][0]
                        if(int(bal) >= int(amount)):
                            if(count == 1):
                                cursorObj.execute("UPDATE SAVINGS_ACCOUNT SET BALANCE = BALANCE - "+str(int(amount))+" WHERE ACCOUNT_ID = " + repr(acc_no))
                            if(count1 == 1):
                                cursorObj.execute("UPDATE CURRENT_ACCOUNT SET BALANCE = BALANCE - "+str(int(amount))+" WHERE ACCOUNT_ID = " + repr(acc_no))
                            if(count2 == 1):
                                cursorObj.execute("UPDATE SAVINGS_ACCOUNT SET BALANCE = BALANCE + "+str(int(amount))+" WHERE ACCOUNT_ID = " + repr(rec_acc_no))
                            if(count3 == 1):
                                cursorObj.execute("UPDATE CURRENT_ACCOUNT SET BALANCE = BALANCE + "+str(int(amount))+" WHERE ACCOUNT_ID = " + repr(rec_acc_no))

                            con.commit()
                            tkinter.messagebox.showinfo( "DONE" , "AMOUNT HAS BEEN TRANSFERRED " )
                            con.close()
                            master.destroy()
                        else:
                            tk.Label(master, text="INSUFFICIENT AMOUNT" , bg = 'red').grid(row=4)      
                    else:
                        tk.Label(master, text="ACCOUNT DOESN'T EXISTS OF RECIPENT" , bg = 'red').grid(row=4)      
                else:
                    tk.Label(master, text="ACCOUNT IS OF DIFFERENT CUSTOMER" , bg = 'red').grid(row=4)  
            else:
                tk.Label(master, text="INVALID ACCOUNT ID" , bg = 'red').grid(row=4)  
            
        else:
            tk.Label(master, text="Amount less than 0" , bg = 'red').grid(row=4)

            
    master = tk.Tk()
    master.title('Banking Managment System')
    tk.Label(master, text="Your Account ID").grid(row=0)
    tk.Label(master, text="Recipent's Account ID").grid(row=1)
    tk.Label(master, text="Amount").grid(row=2)


    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)


    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    tk.Button(master, 
              text='Confirm', command=show_entry_fields).grid(row=5, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)
    tk.mainloop()
 
#transfer_money()
