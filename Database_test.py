import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
    try:
        con = sqlite3.connect('Banking_management.db')
        return con
    except Error:
        print(Error)
 
def sql_table(con):
    cursorObj = con.cursor()
    amount = '10'
    account_id = '1'
    #cursorObj.execute("INSERT INTO CUSTOMER(CUST_ID , PHONE_NUMBER , ADDRESS , FIRST_NAME , LAST_NAME , DATE_OF_BIRTH) VALUES( 100 , '9582242592' , 'Indirapuram' , 'Vatsal' , 'Agarwal' , '1999-12-18')")
    #cursorObj.execute("select * from CUSTOMER")
    #cursorObj.execute("INSERT INTO SAVINGS_ACCOUNT(ACCOUNT_ID , BALANCE , INTEREST_RATE) VALUES( 1 , 10000 , 5)")
    #cursorObj.execute("INSERT INTO DEPOSITS(ACCOUNT_ID , CUST_ID) VALUES( 1 , 100)")
    #cursorObj.execute("UPDATE SAVINGS_ACCOUNT SET BALANCE = BALANCE + "+str(int(amount))+" WHERE ACCOUNT_ID = " + repr(account_id))  
    cursorObj.execute("select * from DEPOSITS")
    row = cursorObj.fetchall()
    print(row)
    cursorObj.execute("select * from CURRENT_ACCOUNT")
    row = cursorObj.fetchall()
    print(row)
    cursorObj.execute("select * from LOAN")
    row = cursorObj.fetchall()
    print(row)
    #print(row.size())
    #print(row[0][0]+row[0][2])
    con.commit()
 
con = sql_connection()
 
sql_table(con)
