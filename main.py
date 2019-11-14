import tkinter
from tkinter import *
#import tkinter.messagebox
import sqlite3
from sqlite3 import Error
from banker_login import *
from customer_login import *
#banker()
def sql_connection():
    try:
        con = sqlite3.connect('Banking_management.db')
        return con
    except Error:
        print(Error)
        
def customerlogin ():
    password = entry2.get()
    username = entry1.get()
    if(username != ''):
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("SELECT COUNT(*) FROM CUSTOMER WHERE CUST_ID = " + username)
        rows = cursorObj.fetchall()
        if(rows[0][0] != 0):
            cursorObj.execute("select * from CUSTOMER where CUST_ID = " + username)
            row = cursorObj.fetchall()
            passw = row[0][0]+row[0][3]
            if(passw == password):
                #login
                #print("hi")
                canvas2.delete("Error1")
                con.close()
                customer(username)
            else:
                canvas1.create_text(150,260,fill="RED",font="Times 10 ",
                                text="INVALID USERNAME OR PASSWORD" , tag = "Error1")
                con.close()
        else:
            canvas1.create_text(150,260,fill="RED",font="Times 10 ",
                            text="INVALID USERNAME OR PASSWORD", tag = "Error1")
            con.close()
    else:
        canvas1.create_text(150,260,fill="RED",font="Times 10 ",
                        text="INVALID USERNAME OR PASSWORD", tag = "Error1")
        con.close()
    
def bankerlogin():
    username = entry3.get()
    password = entry4.get()
    if(username != ''):
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("SELECT COUNT(*) FROM EMPLOYEE1 WHERE EMPLOYEE1.ID = " + username)
        rows = cursorObj.fetchall()
        if(rows[0][0] != 0):
            cursorObj.execute("select * from EMPLOYEE1 where id = " + username)
            row = cursorObj.fetchall()
            passw = row[0][0]+row[0][2]
            if(passw == password):
                #login
                #print("hi")
                canvas2.delete("Error1")
                con.close()
                banker(username)
            else:
                canvas2.create_text(150,260,fill="RED",font="Times 10 ",
                                text="INVALID USERNAME OR PASSWORD" , tag = "Error1")
                con.close()
        else:
            canvas2.create_text(150,260,fill="RED",font="Times 10 ",
                            text="INVALID USERNAME OR PASSWORD", tag = "Error1")
            con.close()
    else:
        canvas2.create_text(150,260,fill="RED",font="Times 10 ",
                        text="INVALID USERNAME OR PASSWORD", tag = "Error1")
        con.close()


main = Tk()

main.geometry("1000x750")
main.configure(background='#00a8ff')
main.title('Banking Managment System')
heading = Label(main ,bg="#fbc531",font="Helvetica 20 bold italic ", text='Welcome to Sinha bank')

heading.pack()



canvas1 = Canvas(main, width = 300, height = 400)
canvas1.pack(side = RIGHT , padx = 40)
#text = Label(canvas1,font="Helvetica 10 bold italic", text='k')

canvas1.create_text(100,40,fill="#2f3640",font="Times 20 italic bold", text="Customer login")
canvas1.create_text(50,140,fill="black",font="Times 10 ", text="ID")
canvas1.create_text(50,190,fill="black",font="Times 10 ", text="PASS")
entry1 = Entry(main) 
canvas1.create_window(140, 140, window=entry1)
entry2 = Entry(main , show="*") 
canvas1.create_window(140, 190, window=entry2)

#text.pack()
    
button1 = Button(text='login', command=customerlogin)
canvas1.create_window(140, 220, window=button1)

#canvas1.coords(entry1 , new_xy)

canvas2 = Canvas(main, width = 300, height = 400)
canvas2.pack(side = LEFT , padx = 40)
canvas2.create_text(100,40,fill="#2f3640",font="Times 20 italic bold", text="Banker login")
canvas2.create_text(50,140,fill="black",font="Times 10 ", text="ID")
canvas2.create_text(50,190,fill="black",font="Times 10 ", text="PASS")
entry3 = Entry(main) 
canvas2.create_window(140, 140, window=entry3)
entry4 = Entry(main , show="*") 
canvas2.create_window(140, 190, window=entry4)

#text.pack()
    
button2 = Button(text='Login', command=bankerlogin)
canvas2.create_window(140, 220, window=button2)

main.mainloop()
