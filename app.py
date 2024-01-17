from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hi Uzair</h1>"
    
@app.route("/about")
def hello_world():
    return "<h1>About page</h1>"
