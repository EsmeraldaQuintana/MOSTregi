import sqlite3 as lite
import sys
import os.path


con = lite.connect('C:\\Users\\E-Winny\\Desktop\\CIS405\\P_N\\MOSTregi\\db.sqlite3')
report= input("What Month is this Report for? ")
print(report)
with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM events_bookingrequest")
    rows = cur.fetchall()
    for row in rows:
        print (row, file=open("C:\\Users\\E-Winny\\Desktop\\CIS405\\P_N\\MOSTregi\\reports\\%s.txt" %report, "a"))
		
