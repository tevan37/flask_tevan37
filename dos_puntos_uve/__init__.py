from flask import Flask
app = Flask(__name__)

@app.route("/")
def hola():
    return 'Hello World'

@app.route("/chau")
def chau():
    return 'Chau'

