from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>HELLO THERE</h1> <h3>you are viewing my website</h3>"
    
@app.route("/<name>/")
def user(name):
    return f"<h1>error</h1> you silly goober, the page {name} probably doesn't exist (or the creator did a dum)"

@app.route("/admin/")
def admin():
    return "youre not an admin >:("

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
