"""
home.py

Home page routes.
"""

from flask import Blueprint
from flask import render_template

from src.applications.oja.modules import MODULES


home_bp = Blueprint(

    "home",

    __name__

)


@home_bp.route("/")
def home():

    return render_template(

        "index.html",

        modules=list(MODULES.keys())

    )