from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/ascii")
def ascii():
    return render_template("ascii.html")


@auth.route("/numbers", methods=["GET", "POST"])
def numbers():
    if request.method == "POST":
        number = request.form.get("number")
        try:
            output = [f"Original (decimal): {number}"]
        except:
            flash("Error", category="error")
            output = []
        return render_template("numbers.html", content=output)
    return render_template("numbers.html")
