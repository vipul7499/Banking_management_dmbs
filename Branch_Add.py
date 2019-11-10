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

def add_branch():
    def show_entry_fields():
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO BRANCH"+ " (BRANCH_ID , BRANCH_NAME , BRANCH_CITY) VALUES(" + e1.get() + ",'" + e2.get() + "','" + e3.get()+ "')")
        con.commit()
        tkinter.messagebox.showinfo( "DONE" , "BRANCH HAS BEEN ADDED " )
        con.close()
        master.destroy()

    master = tk.Tk()
    tk.Label(master, text="Branch id").grid(row=0)
    tk.Label(master, text="Branch name").grid(row=1)
    tk.Label(master, text="Branch City").grid(row=2)

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
#add_branch()
