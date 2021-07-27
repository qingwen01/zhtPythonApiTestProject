from flask import Flask
import json

app = Flask(_name_)

@app.route('/')

def login():
    data = json.dumps({
        "username":"hahah",
        "passworld":"123456"
    })

    return data

if _name_ == "_main_"

login()
