import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app = Flask(__name__)
cnx = mysql.connector.connect(user=os.getenv('MYSQL_USER'), password=os.getenv('MYSQL_PASSWORD'),
                              host=os.getenv('MYSQL_HOST'),
                              database=os.getenv('MYSQL_DATABASE'))

@app.route('/')

def home():
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM USUARIOS")
    databases = cursor.fetchall()
    print(databases)
    response = {"rows": []}
    for item in databases:
        response["rows"].append(item[0])
    print(response)
    cursor.close()
    return response

app.run(host='0.0.0.0',port=50001)