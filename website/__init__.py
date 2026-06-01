import os

from dotenv import load_dotenv
from flask import Flask


def create_application():
    application = Flask(__name__)
    load_dotenv()
    application.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    from .auth import auth
    application.register_blueprint(auth, url_prefix="/")

    return application
