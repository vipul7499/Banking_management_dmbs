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
    cursorObj.execute("create table EMPLOYEE1(ID varchar(20) PRIMARY KEY , NAME varchar(30) , POSITION varchar(30))")
    cursorObj.execute("create table EMPLOYEE2(ID varchar(20) PRIMARY KEY , PHONE_NUMBER VARCHAR(13),FOREIGN KEY (ID) REFERENCES EMPLOYEE1(ID))")
    cursorObj.execute("create table BRANCH(BRANCH_ID varchar(20) PRIMARY KEY , BRANCH_NAME varchar(30) , BRANCH_CITY varchar(30))")
    cursorObj.execute("create table LOAN(LOAN_NO varchar(20) PRIMARY KEY , LOAN_AMOUNT varchar(30) , START_DATE date , END_DATE date , RATE INT(10) , TYPE varchar(30))")
    cursorObj.execute("create table PAYMENT(PAYMENT_NO varchar(20) PRIMARY KEY , PAYMENT_AMOUNT int(10) )")
    cursorObj.execute("create table CUSTOMER(CUST_ID varchar(20) PRIMARY KEY , PHONE_NUMBER varchar(13) , ADDRESS varchar(100) , FIRST_NAME varchar(30) , LAST_NAME varchar(30) , DATE_OF_BIRTH date)")
    cursorObj.execute("create table SAVINGS_ACCOUNT(ACCOUNT_ID varchar(20) PRIMARY KEY , BALANCE int(10) , INTEREST_RATE int(5) )")
    cursorObj.execute("create table CURRENT_ACCOUNT(ACCOUNT_ID varchar(20) PRIMARY KEY , BALANCE int(10) , OVERDRAFT_AMOUNT int(10) )")
    cursorObj.execute("create table FIXED_DEPOSIT(ACCOUNT_ID varchar(20) , INTEREST int(5) , AMOUNT int(10) , TENURE date )")
    


    cursorObj.execute("create table EMPLOYS(ID varchar(20) , BRANCH_ID varchar(20) ,FOREIGN KEY (ID) REFERENCES EMPLOYEE1(ID) , FOREIGN KEY (BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) )")
    cursorObj.execute("create table MANAGES(ACCOUNT_ID varchar(20) , BRANCH_ID varchar(20), FOREIGN KEY (BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) )")
    cursorObj.execute("create table DEPOSITS(ACCOUNT_ID varchar(20) ,  CUST_ID varchar(20), FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER(CUST_ID) )")
    cursorObj.execute("create table BORROWS(LOAN_NO varchar(20) ,  CUST_ID varchar(20), FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER(CUST_ID) , FOREIGN KEY (LOAN_NO) REFERENCES LOAN(LOAN_NO) )")
    cursorObj.execute("create table PROVIDES(BRANCH_ID varchar(20) , LOAN_NO varchar(20), FOREIGN KEY (BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) ,FOREIGN KEY (LOAN_NO) REFERENCES LOAN(LOAN_NO))")
    cursorObj.execute("create table ACCECPTS(PAYMENT_NO varchar(20) , LOAN_NO varchar(20) ,FOREIGN KEY (LOAN_NO) REFERENCES LOAN(LOAN_NO) ,FOREIGN KEY (PAYMENT_NO) REFERENCES PAYMENT(PAYMENT_NO))")
    print(cursorObj)
    
    con.commit()
 
con = sql_connection()
 
sql_table(con)
