import flask
import sqlite3
from flask import request

import smtplib

from datetime import datetime

from random import seed 
from random import choice

app = flask.Flask(__name__)


@app.route('/login', methods=['GET']) 
def login():
    email_address = request.args.get('email_address') 
    password = request.args.get('password') 



    con = sqlite3.connect('my-db.db')

    """if len(restaurant_name) > 0 and len(restaurant_location)>0:
        # insert into db
        insertQuery = f"INSERT INTO Restaurant (restaurant_name,restaurant_location) values (\"{restaurant_name}\",\"{restaurant_location}\");"
        con.execute(insertQuery)
        con.commit()"""

    # select from db
    cursor = con.execute(f"SELECT user_id,email_address, password FROM User WHERE email_address=\"{email_address}\" AND password=\"{password}\";")
    userLoginData = []

    is_there_something_returned = False
    for row in cursor:
        is_there_something_returned = True
        userLoginData.append([row[0],row[1],row[2]]) 
    if not is_there_something_returned:
        userLoginData.append(["Not in database","Not in database","Not in database"])


    con.close()
    outdata = {
        
        "returned_user_id": userLoginData[0][0],
        "returned_email_address": userLoginData[0][1],
        "returned_password": userLoginData[0][2]
    }



    return outdata


@app.route("/passcode",methods=['GET'])
def passcode():
    admin_email_address = "compproject76@gmail.com"
    admin_password = "umrwznsbzjdicnlp"

    email_address = request.args.get('email_address') 

    seed(datetime.now().timestamp())

    my_passcode = [str(choice([i for i in range(10)])) for j in range(6)]
    my_passcode = "".join(my_passcode)


    with smtplib.SMTP("smtp.gmail.com",587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        

        smtp.login(admin_email_address,admin_password)

        subject = "Verify your account for HKU RiceLegFinder"
        body = f"passcode: {my_passcode}"

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(admin_email_address,email_address,msg)

    outdata = {
        
        "passcode": my_passcode
        
    }

    return outdata


    


# adds host="0.0.0.0" to make the server publicly available 
app.run(host="0.0.0.0",port=8964)