
import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "sayakghosh", database = "library")
cursor = con.cursor()
def member_input():
 try:
     memberid=int(input("Enter Member Id"))
     mname = input("Enter Member Name")
     madd = input("Enter member Address")
     phone = input("Enter Phone No")

     qry = "insert into member values({},'{}','{}','{}');".format(memberid, mname, madd, phone)
     cursor.execute(qry)
     con.commit()
     print("added successfully..")
 except:
     print("Error...")
def member_edit():
 x=int(input("Enter Member ID"))
 qry="select * from member where memberid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
     y=input("Enter New Address")
     qry = "update member set madd = '{}' where memberid = {};".format(y,x)
     cursor.execute(qry)
     con.commit()
     print("Edited Successfully.")

 else:
     print("Wrong Member ID")
def member_delete():

 x=int(input("Enter Member ID"))
 qry="select * from member where memberid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
     qry = "delete from member where memberid = {};".format(x)
     cursor.execute(qry)
     con.commit()
     print("deleted Successfully.")

 else:
     print("Wrong member ID")
def member_search():
     x=int(input("Enter Member ID"))
     qry="select * from member where memberid = {};".format(x)
     cursor.execute(qry)
     r = cursor.fetchone()
     if r:
         df = pd.read_sql(qry, con)
         print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

     else:
         print("Wrong Member ID")