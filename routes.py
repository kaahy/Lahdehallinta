from flask import redirect, render_template, request
from app import app
from repositories import books_repository
from services import source_service

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add(inserter=source_service.insert_book):
    if request.method == "GET":
        return render_template("add.html")
    
    if request.method == "POST":
        tag = request.form["tag"]
        title = request.form["title"]
        author = request.form["author"]
        publish_year = request.form["publish_year"]
        publisher = request.form["publisher"]
        inserter(tag, title, author, publish_year, publisher, books_repository)

        return render_template("add.html")

@app.route("/list", methods=["GET"])
def list_sources():
    books = source_service.get_books(books_repository)
    return render_template("list.html", sources=books)