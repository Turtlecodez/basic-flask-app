from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>HELLO THERE</h1> /n <h3>you are viewing my website</h3>"
    
@app.route("/<name>")
def user(name):
    return f"you silly goober, the page /"{name}/" doesn't exist lol"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
