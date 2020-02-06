# import flask
from flask import Flask, render_template

# instantiate instance of Flask class
app = Flask(__name__)

# route 1: homepage
@app.route("/")
def welcome():
    return render_template("index.html")


# runs app and allows us to debug
if __name__ == "__main__":
    app.debug = True
    app.run()
