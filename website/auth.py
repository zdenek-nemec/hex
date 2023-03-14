from flask import Blueprint, render_template, request, flash

from website.hex import Hex
from website.uli import Uli

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/hex", methods=["GET", "POST"])
def hex():
    if request.method == "POST":
        number = request.form.get("number")
        try:
            hex = Hex(number)
            output = [
                f"Original (decimal): {number}",
                f"Binary: {hex.get_value(2)}",
                f"Hexadecimal: {hex.get_value(16)}"
            ]
        except:
            flash("Invalid value", category="error")
            output = []
        return render_template("hex.html", content=output)
    return render_template("hex.html")


@auth.route("/uli", methods=["GET", "POST"])
def uli():
    if request.method == "POST":
        uli = Uli(request.form.get("uli"))
        if not uli.is_valid():
            flash("Invalid ULI", category="error")
        return render_template("uli.html", formatted_uli=uli.get_formatted_uli(), details=uli.get_uli_details())
    return render_template("uli.html")
