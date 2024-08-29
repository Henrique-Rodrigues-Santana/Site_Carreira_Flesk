from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def ola_mundo():
    return "Olá, mundo!"
@app.route("/ola")
def primeira():
    return render_template("home.html")


app.run(debug=True)