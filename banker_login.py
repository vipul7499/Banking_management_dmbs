from tkinter import *
import sqlite3
from sqlite3 import Error
from PIL import ImageTk , Image
import tkinter
import tkinter.messagebox
from Create_Customer import *
from Print_All_Customers import *
from Open_Account import *
from Branch_Add import *
from List_Branch import *
from Add_Employee import *
from List_Employee import *
from Create_Fd import * 
from Apply_Loan import *



def sql_connection():
    try:
        con = sqlite3.connect('Banking_management.db')
        return con
    except Error:
        print(Error)
        
def banker(banker_id):
    def banker_jobs():
        choice = v.get()
        if v.get() == '1':
            create_customer()

        if v.get() == '2':
            open_account()

        if v.get() == '3':
            give_loan()

        if v.get() == '4':
            add_employee()

        if v.get() == '5':
            list_employees()

        if v.get() == '6':
            create_fd()
            
        if v.get() == '7':
            print_customer()
            
        if v.get() == '8':
            add_branch()

        if v.get() == '9':
            print_branch()
            
       
    global img
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("select * from EMPLOYEE1 where id = " + banker_id)
    rows = cursorObj.fetchall()
    name = rows[0][1]
    root=Toplevel()
    root.title('Sinha Bank')
    root.geometry("1000x750+10+20")
    root.configure(background='light green')


    heading = Label(root ,bg="blue",font="Helvetica 20 bold italic", text='Welcome to Sinha bank')
    heading.place(x=330, y=10)

    profile_banker = Canvas(root, width = 300, height = 520)
    profile_banker.pack(side = LEFT , padx = 40)
    img = ImageTk.PhotoImage( file="face1.png")
    profile_banker.create_image(80,20, anchor=NW, image=img)  


    profile_banker.create_text(135,170,fill="darkblue",font="Times 20 italic bold",
                            text=name)
    

    canvas1 = Canvas(root, width = 520, height = 100)
    canvas1.pack(side = TOP, pady = 103 )
    
    v = StringVar(root, "1") 
      
    values = {"Add customer" : "1",
              "Open account" : "2", 
              "Apply for Loan" : "3", 
              "Add Employee" : "4", 
              "List All Employee" : "5", 
              "Apply for FD" : "6",
              "List All Customers":"7" ,
              "Add Branch":"8" ,
              "List All Branch":"9"} 
      
    for (text, value) in values.items(): 
        Radiobutton(root, text = text, variable = v,  
                    value = value, indicator = 0,command=banker_jobs ,
                    background = "light blue").pack(fill = X, ipady = 5) 
    #profile_banker.pack()
    root.mainloop()
#banker(str(10))    
