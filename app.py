from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return {"message": "Hello World!"}

app.run(host='0.0.0.0',port=50001)