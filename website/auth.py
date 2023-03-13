from flask import Blueprint, render_template, request
from website.uli import Uli

auth = Blueprint("auth", __name__)


@auth.route("/hex", methods=["GET", "POST"])
def hex():
    if request.method == "POST":
        number = request.form.get("number")
        return render_template("hex.html", submitted=True, number=number)
    return render_template("hex.html")


@auth.route("/uli", methods=["GET", "POST"])
def uli():
    if request.method == "POST":
        uli = request.form.get("uli")
        return render_template("uli.html", submitted=True, content=Uli(uli).get_uli_readable())
    return render_template("uli.html")
