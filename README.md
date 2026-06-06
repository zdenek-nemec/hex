# Hex

---

# Project Description

## Structure and Tools

[GitHub: Hex](https://github.com/zdenek-nemec/hex)

* Project
* Repository
* Issues

Python 3.12

* Works on newer Python as well. Version 3.12 selected to be compatible with [PythonAnywhere](https://www.pythonanywhere.com/).

Development environment

* IDE: [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)
* Virtual environment manager: [uv](https://docs.astral.sh/uv/)

---

# To Do List

* [x] Set up project
* [x] Create repository
* [x] Hello-World
* [x] Update dependencies
* [ ] Cleanup old files
* [x] Publish
* [x] Update `flask_app.py` for PA
* [ ] Website
* [ ] `#3` Numbers
  * [x] Numbers page 
  * [x] Number class 
  * [x] Validation
  * [x] Formatting output
  * [x] Conversion 10 to 2/8/16
  * [ ] Conversion 2/8/16 to 10
  * [ ] Allow to input any base on Numbers page
* [ ] ULI (ToN, Cell ID)
* [ ] Logging
* [ ] Selenium tests
* [ ] Docker
* [ ] API
* [ ] Pipeline
* [ ] Add "How to build and run" to the README.md
* [ ] `#23` Code cleanup
   * [x] Remove legacy modules
   * [x] Remove legacy code from kept modules
   * [ ] Remove non-solution tests
* [x] `#26` Secure SECRET_KEY
* [ ] `#27` CVEs
* [x] `#29` ASCII

Other

* [ ] Fix the error stripe (Numbers). Do not obscure main menu. Do not move page layout down.
* [ ] Bigger font for Numbers > Result.
* [ ] Selenium tests for ASCII
* [ ] Selenium tests for Numbers

---

# How to Build and Run

1. Clone the repository from [https://github.com/zdenek-nemec/hex](https://github.com/zdenek-nemec/hex)
2. Import the project to PyCharm (to-be-updated)
3. Install dependencies (to-be-updated)
4. Set environment variable `SECRET_KEY` (see section "SECRET_KEY")
5. Run the application via `flask_app.py`
6. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in web browser

## SECRET_KEY

For development the `SECRET_KEY` can be temporarily hard-coded in `website/__init__.py`.

```python
SECRET_KEY="change-me"
```

For all other purposes set it via environment.

1. In repository home directory create `.env` file with variable `SECRET_KEY`

    ```dotenv
    SECRET_KEY=change-me
    ```

2. In PyCharm edit `flask_app` configuration and set "Paths to .env files" to the `.env` file (e.g. `/home/zdenek/Git/hex/.env`)<br />![PyCharm Configuration](documentation/pycharm_configuration.png)

---

# Legacy code

## `flask_app.py`

```python
if __name__ == "__main__":
    # argument_parser = argparse.ArgumentParser()
    # argument_parser.add_argument("--debug", action="store_true")
    # application = create_application()
    # application.run(debug=argument_parser.parse_args().debug)
    app.run(debug=False)
```

## `website/auth.py`

```python
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
```
