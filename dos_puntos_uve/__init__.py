from flask import Flask
app = Flask(__name__)

@app.route("/")
def hola():
    return 'Hello World'

@app.route("/Daighax")
def chau():
    return 'I hate niggers'