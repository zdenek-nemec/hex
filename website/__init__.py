from flask import Flask


def create_application():
    application = Flask(__name__)
    application.config["SECRET_KEY"] = "hex"

    from .auth import auth
    application.register_blueprint(auth, url_prefix="/")

    return application
