from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/<name>/")
def user(name):
    return f"<h1 style="text-align:center">error</h1> <h3>the page {name} does not exist, or Turtlecodez did a dum.</h3>"

@app.route("/games/")
def games():
    return render_template("games.html")

@app.route("/admin/")
def admin():
    return "youre not an admin >:("

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
