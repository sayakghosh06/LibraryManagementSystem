import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "sayakghosh", database = "library")
cursor = con.cursor()
def book_input():
 try:
    bookid=input("Enter Book Id")
    bname = input("Enter Book Name")
    author = input("Enter Author Name")
    price = float(input("Enter Price"))
    copies = int(input("Enter No of Copies"))
    qry = "insert into book values({},'{}','{}',{},{},{});".format(bookid, bname, author, price,copies,copies)
    cursor.execute(qry)
    con.commit()
    print("added successfully..")
 except:
    print("Error.. Worng Entry")
def book_edit():
 x=int(input("Enter Book ID"))
 qry="select * from book where bookid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
     y=float(input("Enter New Price"))
     qry = "update book set price = {} where bookid = {};".format(y,x)
     cursor.execute(qry)
     con.commit()
     print("Edited Successfully.")

 else:
     print("Wrong Book ID")
def book_update():

 x=int(input("Enter Book ID"))
 qry="select * from book where bookid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 print("Present Copies- ",r[4])
 print("Present Remaining Copies- ",r[5])
 if r:
     y=float(input("Enter No of New Copies"))
     qry = "update book set copies = {}, rem_copies = {} where bookid ={};".format(r[4]+5,r[5]+5,x)
     cursor.execute(qry)
     con.commit()
     print("Updated Successfully.")
     qry="select * from book where bookid = {};".format(x)
     df = pd.read_sql(qry,con)
     print("New Updated Book Details")
     print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
 else:
     print("Wrong Book ID")
def book_delete():
 x=int(input("Enter Book ID"))
 qry="select * from book where bookid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
     qry = "delete from book where bookid = {};".format(x)
     cursor.execute(qry)
     con.commit()
     print("deleted Successfully.")

 else:
     print("Wrong Book ID")
def book_search():
 x=int(input("Enter Book ID"))
 qry="select * from book where bookid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:

     df = pd.read_sql(qry,con)
     print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))


 else:
     print("Wrong Book ID")