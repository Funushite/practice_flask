from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def menu():
  return render_template("menu.html")