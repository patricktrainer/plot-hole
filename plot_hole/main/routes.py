from flask import render_template, url_for, flash, redirect, request, Blueprint

main = Blueprint("main", __name__)


@main.route("/", methods=("GET", "POST"))
def home():
    return render_template("home.html")


@main.route("/about")
def about():
    return render_template("about.html")
