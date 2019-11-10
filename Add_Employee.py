import tkinter as tk
from tkinter import *
from datetime import date
import sqlite3
from sqlite3 import Error
import tkinter
import tkinter.messagebox

def add_employee():
    def sql_connection():
        try:
            con = sqlite3.connect('Banking_management.db')
            return con
        except Error:
            print(Error)
    def show_entry_fields():
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("SELECT count(*) FROM BRANCH WHERE BRANCH_ID = "+e1.get())
        row = cursorObj.fetchall()
        if(row[0][0] != 0):    
            cursorObj.execute("SELECT count(*) FROM EMPLOYEE1")    
            row1 = cursorObj.fetchall()
            emp_id = str(date.today())
            emp_id = ''.join(emp_id.split('-'))
            emp_id = emp_id+str(row1[0][0]) + '4'
            cursorObj.execute("INSERT INTO EMPLOYEE1"+ " (ID , NAME , POSITION) VALUES(" + emp_id + ",'" + e2.get() + "','" + e3.get()+ "')")
            cursorObj.execute("INSERT INTO EMPLOYS"+ " (ID , BRANCH_ID) VALUES(" + emp_id + "," + e1.get() + ")")
            con.commit()
            phno = e4.get()
            phno = phno.split(',')
            for i , no in enumerate(phno):
                cursorObj.execute("INSERT INTO EMPLOYEE2"+ " (ID , PHONE_NUMBER) VALUES(" + emp_id + ",'" + no+ "')")
            tkinter.messagebox.showinfo( "DONE" , "EMPLOYEE ID is : " + emp_id)
            con.close()
            master.destroy()
        else:
            error5 = tk.Label(master, text="INVALID BRANCH ID" , bg = 'red')
            error5.grid(row=4)

    master = tk.Tk()
    tk.Label(master, text="Branch id").grid(row=0)
    tk.Label(master, text="Name").grid(row=1)
    tk.Label(master, text="Position").grid(row=2)
    tk.Label(master, text="Phone Number(comma seperated)").grid(row=3)
    
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
#add_employee()
