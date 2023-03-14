from flask import Flask

SECRET_KEY = "$aT0Im!S4$YGkD14CZvQ!h%v$gr9gGayA6qgeVHV#W86zLBXLNT#tgn*irBtC&$M"


def create_application():
    application = Flask(__name__)
    application.config["SECRET_KEY"] = SECRET_KEY

    from .auth import auth
    application.register_blueprint(auth, url_prefix="/")

    return application
