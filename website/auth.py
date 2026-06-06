from flask import Blueprint, render_template, request, flash

from number import Number

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/ascii")
def ascii_page():
    return render_template("ascii.html")


@auth.route("/numbers", methods=["GET", "POST"])
def numbers():
    if request.method == "POST":
        number = request.form.get("number")
        output = []
        if number is not None:
            try:
                output = Number(number).format()
            except ValueError as e:
                flash(f"Error: {e}", category="error")
        return render_template("numbers.html", content=output)
    return render_template("numbers.html")
