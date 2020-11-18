from flask import Flask
app = flask(__name__)

@app.route('/hello/<name')
def hello_name(name):
    return {"hello":name}

@app.route('/')
def hell_world():
    return 'Hello, World'