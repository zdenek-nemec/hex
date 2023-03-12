from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__)


@auth.route("/hex", methods=["GET", "POST"])
def hex():
    if request.method == "POST":
        number = request.form.get("number")
        return render_template("hex.html", submitted=True, number=number)
    return render_template("hex.html")


@auth.route("/uli")
def uli():
    return render_template("uli.html")
