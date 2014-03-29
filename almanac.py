from flask import Flask
from flask import render_template

app = Flask(__name__)


#Create our index or root / route
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/authors")
def authors():
    return render_template("authors.html")


@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")


@app.route("/contents")
def contents():
    return render_template("contents.html")


@app.route("/contest/rules")
def contest_rules():
    return render_template("contest/rules.html")


if __name__ == "__main__":
    app.run(debug="True")
