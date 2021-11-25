from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/reg")
def reg():
    return render_template("registration.html")

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5000, debug =True)