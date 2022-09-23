import Book
import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "sayakghosh", database = "library")
cursor = con.cursor()
def book_issue():
 q = "select max(issueid) from issue;"
 cursor.execute(q)
 r = cursor.fetchone()[0]
 if r:
  issueid = r+1
 else:
  issueid = 1
 x=int(input("Enter Member ID"))
 q1 = "select * from member where memberid = {};".format(x)
 cursor.execute(q1)
 r=cursor.fetchone()
 if r:
   y =int(input("Enter Book ID"))
   q2 = "select bookid, rem_copies from book where bookid = {};".format(y)
   cursor.execute(q2)
   r=cursor.fetchone()
   if r:
     if r[1] > 0:
       issuedate = input("Enter Issue Date")
       copies = int(input("Enter No of Copies"))
       remcopies = r[1] - copies
       q3 = "insert into issue values({},'{}',{},{},{});".format(issueid, issuedate, x, y,copies)
       cursor.execute(q3)
       q4 = "update book set rem_copies = {} where bookid = {};".format(remcopies,y)
       cursor.execute(q4)
       con.commit()
       print("Book Issued...")
     else:
       print("Book is Not Available")
   else:
     print("Wrong Book ID ")

 else:
   print("Wrong Memeber Id")

def book_return():
 q = "select max(returnid) from returns;"
 cursor.execute(q)
 r = cursor.fetchone()[0]
 if r:
   reutrnid = r+1
 else:
   returnid = 1
 x=int(input("Enter Member ID"))
 q1 = "select * from member where memberid = {};".format(x)
 cursor.execute(q1)
 r=cursor.fetchone()
 if r:
    y =int(input("Enter Book ID"))
    q2 = "select bookid, rem_copies from book where bookid = {};".format(y)
    cursor.execute(q2)
    r=cursor.fetchone()
    if r:
        returndate = input("Enter return Date")
        copies = int(input("Enter No of Copies"))
        remcopies = r[1] + copies
        q3 = "insert into returns values({},'{}',{},{},{});".format(returnid, returndate, x, y,copies)
        cursor.execute(q3)
        q4 = "update book set rem_copies = {} where bookid = {};".format(remcopies,y)
        cursor.execute(q4)
        con.commit()
        print("Book Returned...")

    else:
       print("Wrong Book ID ")

 else:
    print("Wrong Memeber Id")