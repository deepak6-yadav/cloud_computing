#!/usr/bin/python2

import cgi
import cgitb
import mysql.connector as mariadb	#importing mariadb

cgitb.enable()

print "content-type:text/html"	#header for printing to html page
print ""



data=cgi.FormContent()

username=data['uname'][0]
password=data['upass'][0]

x=mariadb.connect(user='root', password='redhat', database='lw')

y=x.cursor() #creating a cursor to the database object x

sql="select username,passwd from users where username=%s" #searching for username password for the particular user DB

y.execute(sql,(username,))

result=y.fetchone()

trigger=str(result)

if(trigger=='None'):	#check whether username present or not
	print ("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.112/error.html\">\n")


else :		

	usr=result[0]
	passwd=result[1]
	
	if(password==passwd):
		print ("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.112/reservice.html\">\n") #rechoose service
	else:
		print ("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.112/error.html\">\n")	
		
























































































































































































































































































































































































































		
	

	
