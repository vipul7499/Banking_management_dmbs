from tkinter import *
import sqlite3
from sqlite3 import Error
from View_Accounts import *
from View_All_FD import *
from View_All_Loan import *
from transfer_money import *
from withdraw import *
import tkinter
import tkinter.messagebox

def sql_connection():
    try:
        con = sqlite3.connect('Banking_management.db')
        return con
    except Error:
        print(Error)
def customer(customer_id):
    def bankerlogin():
        account_id = Account.get()
        amount = Amount.get()
        #amount = int(amount)
        account_type = Account_type.get()
        if(account_id != ''):
            con = sql_connection()
            cursorObj = con.cursor()
            cursorObj.execute("SELECT COUNT(*) FROM "+account_type+" WHERE ACCOUNT_ID = " + repr(account_id))
            rows = cursorObj.fetchall()
            if(rows[0][0] != 0):
                cursorObj.execute("select *  FROM "+account_type+" WHERE ACCOUNT_ID = " + repr(account_id))
                if(int(amount) >= 0):
                    #login
                    cursorObj.execute("UPDATE "+account_type+" SET BALANCE = BALANCE + "+str(int(amount))+" WHERE ACCOUNT_ID = " + repr(account_id))
                    header_banker.delete("Error2")
                    header_banker.delete("Error3")
                    tkinter.messagebox.showinfo( "DONE" , "Amount has been debited.")
                    print("hi")
                    con.commit()
                    con.close()
                else:
                    header_banker.create_text(250,90,fill="RED",font="Times 10 ",
                                    text="ENTER AMOUNT GREATER THAN 0" , tag = "Error3")
                    con.close()
            else:
                header_banker.create_text(250,90,fill="RED",font="Times 10 ",
                                text="INVALID ACCOUNT NUMBER", tag = "Error2")
                con.close()
        else:
            header_banker.create_text(250,90,fill="RED",font="Times 10 ",
                            text="INVALID ACCOUNT NUMBER", tag = "Error2")
            con.close() 
    def customerlogin ():
        loan_id = loan.get()
        amount = Amount.get()
        account_id = Account.get()
        if(loan != ''):
            con = sql_connection()
            cursorObj = con.cursor()
            cursorObj.execute("SELECT COUNT(*) FROM LOAN WHERE LOAN_NO = " + repr(loan_id))
            rows = cursorObj.fetchall()
            count = rows[0][0]
            cursorObj.execute("SELECT COUNT(*) FROM SAVINGS_ACCOUNT WHERE ACCOUNT_ID = " + account_id)
            rows = cursorObj.fetchall()
            count = count + rows[0][0]
            if(rows[0][0] != 0):
                acc_type = "SAVINGS_ACCOUNT"
            else:
                acc_type = "CURRENT_ACCOUNT"
            cursorObj.execute("SELECT COUNT(*) FROM CURRENT_ACCOUNT WHERE ACCOUNT_ID = " + account_id)
            rows = cursorObj.fetchall()
            count = count + rows[0][0]
            ac = 2
            print(count)
            cursorObj.execute("SELECT * FROM LOAN WHERE LOAN_NO = " + repr(loan_id))
            loan_det = cursorObj.fetchall()
            if(count >= 2 ):
                cursorObj.execute("select *  FROM "+acc_type+" WHERE ACCOUNT_ID = " + repr(account_id))
                det = cursorObj.fetchall()
                if(int(amount) >= 0):
                    if(int(loan_det[0][1])-int(amount) >= 0):
                        if(int(det[0][1]) - int(amount) >= 0):
                            cursorObj.execute("UPDATE "+acc_type+" SET BALANCE = BALANCE - "+str(int(amount))+" WHERE ACCOUNT_ID = " + repr(account_id))
                            cursorObj.execute("UPDATE LOAN SET LOAN_AMOUNT = LOAN_AMOUNT - "+str(int(amount))+" WHERE LOAN_NO = " + repr(loan_id))
                            canvas1.delete("Error2")
                            canvas1.delete("Error3")
                            tkinter.messagebox.showinfo( "DONE" , "Amount has been debited.")
                            print("hi")
                            con.commit()
                            con.close()
                        else:
                            canvas1.create_text(250,90,fill="RED",font="Times 10 ",
                                        text="INSUFFICIENT AMOUNT IN ACCOUNT" , tag = "Error3")
                    else:
                            canvas1.create_text(250,90,fill="RED",font="Times 10 ",
                                        text="YOU ARE PAYING EXTRA" , tag = "Error3")
                    con.close()  
                else:
                    canvas1.create_text(250,90,fill="RED",font="Times 10 ",
                                    text="ENTER AMOUNT GREATER THAN 0" , tag = "Error3")
                    con.close()
            else:
                canvas1.create_text(250,90,fill="RED",font="Times 10 ",
                                text="INVALID LOAN NUMBER/ACCOUNT NUMBER", tag = "Error2")
                con.close()
        else:
            canvas1.create_text(250,90,fill="RED",font="Times 10 ",
                            text="INVALID LOAN/ACCOUNT NUMBER", tag = "Error2")
            con.close() 
    def customer_jobs():
        choice = v.get()
        if v.get() == '1':
            view_all_account(customer_id)

        if v.get() == '2':
            view_loan(customer_id)

        if v.get() == '3':
            view_fd(customer_id)
        if v.get() == '4':
            transfer_money(customer_id)
        if v.get() == '5':
            withdrawal(customer_id)
        
    main=Toplevel()
    main.title('Sinha Bank')
    main.geometry("1000x750+10+20")
    main.configure(background='light green')

    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM CUSTOMER WHERE CUST_ID = " + str(customer_id))
    detail = cursorObj.fetchall()
    
    heading = Label(main ,bg="blue",font="Helvetica 20 bold italic", text='Welcome to Sinha bank')
    heading.place(x=330, y=10)

    #heading.pack()


    #canvas1.coords(entry1 , new_xy)

    canvas2 = Canvas(main, width = 300, height = 540)
    canvas2.pack(side = LEFT , padx = 40)
    #entry2 = Entry(main) 
    #canvas2.create_window(100, 140, window=entry2)
    img = PhotoImage(file="face1.png")
    canvas2.create_image(80,20, anchor=NW, image=img)  
    canvas2.create_text(135,170,fill="darkblue",font="Times 20 italic bold",
                            text=detail[0][3]+" "+detail[0][4])
    canvas2.create_text(135,210,font="Times 15",
                            text=detail[0][0])




    canvas1 = Canvas(main, width = 520, height = 100)
    canvas1.pack(side = TOP, pady = 90 )
    loan = Entry(main)
    canvas1.create_text(125,20,fill="black",font="Times 13 ",
                            text="Enter the amount to be deposited")
    canvas1.create_window(210, 45, window=loan)
    canvas1.create_text(75,45,fill="black",font="Times 13 ",
                            text="Loan Number")
    Amount = Entry(main)
    canvas1.create_window(210, 65, window=Amount)
    canvas1.create_text(75,65,fill="black",font="Times 13 ",
                            text="Amount")
    Account = Entry(main)
    canvas1.create_window(440, 50, window=Account)
    canvas1.create_text(330,50,fill="black",font="Times 13 ",
                            text="Account No")
    
    deposit_btn = Button(canvas1, text='APPROVE', command=customerlogin)
    canvas1.create_window(420, 90, window=deposit_btn)

    header_banker = Canvas(main, width = 520, height = 100)
    header_banker.pack(side = TOP, pady = 10 )
    Account = Entry(main)
    header_banker.create_text(125,20,fill="black",font="Times 13 ",
                            text="Enter the amount to be deposited")
    header_banker.create_window(210, 45, window=Account)
    header_banker.create_text(75,45,fill="black",font="Times 13 ",
                            text="Account Number")
    Amount = Entry(main)
    header_banker.create_window(210, 65, window=Amount)
    header_banker.create_text(75,65,fill="black",font="Times 13 ",
                            text="Amount")

    Account_type = StringVar(header_banker)
    Account_type.set("SAVINGS_ACCOUNT") 

    option = OptionMenu(header_banker, Account_type, "SAVINGS_ACCOUNT", "CURRENT_ACCOUNT")
    header_banker.create_window(400, 50, window=option)
    
    deposit_btn = Button(header_banker, text='ADD', command=bankerlogin)
    header_banker.create_window(420, 90, window=deposit_btn)

    v = StringVar(main, "1") 
      
    # Dictionary to create multiple buttons 
    values = {"View All Accounts" : "1", 
              "View loan Repayment " : "2", 
              "View Fixed deposits" : "3",
              "Transfer Money" : "4" ,
              "Withdrawal" : "5"}
      
    # Loop is used to create multiple Radiobuttons 
    # rather than creating each button seperately 
    for (text, value) in values.items(): 
        Radiobutton(main, text = text, variable = v,  
                    value = value, indicator = 0,command=customer_jobs ,
                    background = "light blue").pack(fill = X, ipady = 5) 

    main.mainloop()
#customer('100')
