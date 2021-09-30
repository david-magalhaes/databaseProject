import mysql.connector
from flask import Flask

app = Flask(__name__)
cnx = mysql.connector.connect(user='root', password='020290', host='localhost', database='flask')

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