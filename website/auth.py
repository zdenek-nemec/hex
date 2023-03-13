from flask import Blueprint, render_template, request, flash
from website.uli import Uli

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/hex", methods=["GET", "POST"])
def hex():
    if request.method == "POST":
        number = request.form.get("number")
        return render_template("hex.html", submitted=True, number=number)
    return render_template("hex.html")


@auth.route("/uli", methods=["GET", "POST"])
def uli():
    if request.method == "POST":
        uli = Uli(request.form.get("uli"))
        if not uli.is_valid():
            flash("Empty or invalid ULI", category="error")
        return render_template("uli.html", submitted=uli.is_valid(), formatted_uli=uli.get_formatted_uli(),
                               details=uli.get_uli_details())
    return render_template("uli.html")
