from entity.Book import Book
from flask import Flask, render_template, redirect
from flask.helpers import url_for
from jinja2 import Environment
from setting import session

env = Environment(variable_start_string="${", variable_end_string="}")
app = Flask(__name__)

@app.route("/book/list", methods=["GET"])
def list():
    """
    図書一覧
    """
    books = session.query(Book).all()
    return render_template("book/list.html", books=books)

@app.route("/member/create", methods=["GET"])
def entry():
    """
    ユーザー登録
    """
    return render_template("member/entry.html")

@app.route("/member/create", methods=["POST"])
def create():
    return redirect(url_for("/book/list"))