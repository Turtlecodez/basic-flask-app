from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/<name>/")
def user(name):
    return f"<h1>error</h1> you silly goober, the page {name} probably doesn't exist (or the creator did a dum)"

@app.route("/admin/")
def admin():
    return "youre not an admin >:("

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
