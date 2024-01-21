from flask import Flask, render_template, request
import calculate

app = Flask(__name__)

@app.route("/")
def menu():
  return render_template("menu.html")

#ベース
@app.route("/calculate/", methods=["GET", "POST"])
def cal():
  if request.method=="POST":
    ans = 0
    var_a = 0
    var_b = 0
    var_a = request.form.get("var_a", type=int)
    var_b = request.form.get("var_b", type=int)
    if type(var_a) is not int:
      var_a = 0
    if type(var_b) is not int:
      var_b = 0

    mode = request.form.get("mode")
    if mode == "plus":
      ans = calculate.plus(var_a, var_b)
    elif mode == "mlt_by":
      ans = calculate.mlt_by(var_a, var_b)
    
    return render_template("calculate.html", ans=str(ans), var_a=str(var_a), var_b=str(var_b))
  else:
    return render_template("calculate.html")

@app.route("/hello/", methods=["GET", "POST"])
def hello():
  return render_template("hello.html")