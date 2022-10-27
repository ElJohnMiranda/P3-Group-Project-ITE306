'''Title: Coffee Shop Website
    Description: A website you can visit if you want to buy the coffee you like.
    Programmers:
    1. El John g Miranda
    2. John Dave Badua
    3. Richard Dolores
    4. Vincent Urance
    5. Warren Bercasio'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/product")
def product():
    return render_template("product.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()

