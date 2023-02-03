#!/usr/bin/env python3
#Query the miRNA database through the browser using a cgi program

import pymysql
import cgi
import cgitb
import json

#the next line is useful for debugging
#it causes errors during execution to be sent back to the browser
cgitb.enable()

#retrieve input data from the web server
form = cgi.FieldStorage() 

#next line is always required as first part of http output
print("Content-type: text/html\n")

if (form):
    #establish the connection on bioed
    connection = pymysql.connect(host='bioed.bu.edu',user='resh10',password='PadmaRam_10', db='miRNA',port = 4253)  
    cursor = connection.cursor()
    #get submitted values
    miRNA = form.getvalue("miRNA_name")
    seq = form.getvalue("miRNA_seq")
    selector = form.getvalue("selector","")

    if (selector == "miRNA_histogram"):
        query1 = "select score from miRNA join targets using(mid) where name = %s order by score"
        #execute query
        try: 
            cursor.execute(query1,[miRNA])
        except pymysql.Error as e: 
            print(e,query1)
        results = cursor.fetchall() 
        #format the output as json object
        print(json.dumps(results))
    
    elif (selector == "miRNA_table"):
        query2 = "select name, seq from miRNA where seq regexp %s"
        #execute query
        try: 
            cursor.execute(query2,[seq])
        except pymysql.Error as e: 
            print(e,query2)
        results = cursor.fetchall() 
        #format the output as json object
        print(json.dumps(results))
    cursor.close()
    connection.close()