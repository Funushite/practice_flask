from flask import Flask, render_template, request
import calculate

app = Flask(__name__)

@app.route("/")
def menu():
  return render_template("menu.html")

#ベース
@app.route("/calculate/", methods=["GET", "POST"])
def cal():
  modes = ["","","",""]
  if request.method=="POST":
    var_a = request.form.get("var_a", type=int)
    var_b = request.form.get("var_b", type=int)
    index_mode = request.form.get("mode", type=int)
    modes[index_mode] = "checked"

    ans = calculate.regulate(var_a, var_b, index_mode)
    
    return render_template("calculate.html", modes=modes, ans=str(ans), var_a=str(var_a), var_b=str(var_b))
  else:
    modes = ["checked","","",""]

    return render_template("calculate.html", modes=modes)

@app.route("/hello/", methods=["GET", "POST"])
def hello():
  return render_template("hello.html")