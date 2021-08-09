from flask import Flask, render_template, request
from jinja2 import Environment

env = Environment(variable_start_string="${", variable_end_string="}")
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html")
