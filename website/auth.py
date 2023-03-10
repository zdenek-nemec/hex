from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/hex")
def hex():
    return render_template("hex.html")


@auth.route("/uli")
def uli():
    return render_template("uli.html")
