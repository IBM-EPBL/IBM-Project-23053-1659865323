from flask import Flask, render_template, request, redirect, session 
import re

from flask_db2 import DB2
import ibm_db
import ibm_db_dbi
from sendgrid import *
import os


app.config['database'] = 'bludb'
app.config['hostname'] = '8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud'
app.config['port'] = '30120'
app.config['protocol'] = 'tcpip'
app.config['uid'] = 'fsd14997'
app.config['pwd'] = '7JR2ia5UzeAseRvL'
app.config['security'] = 'SSL'
try:
    mysql = DB2(app)

    conn_str='DATABASE=bludb;HOSTNAME=8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;SECURITY=SSL;PORT=30120;PROTOCOL=TCPIP;UID=fsd14997;PWD=7JR2ia5UzeAseRvL'
    ibm_db_conn = ibm_db.connect(conn_str,'','')
        
    print("Database connected without any error !!")
except:
    print("IBM DB Connection error   :     " + DB2.conn_errormsg()) 
    
    msg = "Hello " + session['username'] + " , " + "you have crossed the monthly limit of Rs. " + str(s) + "/- !!!" + "\n" + "Thank you, " + "\n" + "Team Experte"  
        #sendmail(msg,session['email'])  
        sg = sendgrid.SendGridAPIClient(api_key='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')
        from_email = Email("balajinrcse2022@gmail.com")
        cusmail = session['email']
        to_email = To(cusmail)
        content = Content("text/html", msg)
        subject = "Limit alert !!! - Experte"
    
        mail = Mail(from_email, to_email, subject, content)
        mail_json = mail.get()
        response = sg.client.mail.send.post(request_body=mail_json)
    
