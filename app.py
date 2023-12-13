from flask import Flask, render_template
import redirect
import url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<title>turtle's test site</title> <h1>turtle's test site</h1> <h3>a site that turtle uses to test things</h3> <h4>yeah</h4>"
    
@app.route("/<name>/")
def user(name):
    return f"<h1>error</h1> you silly goober, the page {name} probably doesn't exist (or the creator did a dum)"

@app.route("/admin/")
def admin():
    return "youre not an admin >:("

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
