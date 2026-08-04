"""
home.py

Home page routes.
"""

from flask import Blueprint
from flask import render_template

from src.applications.oja.modules import MODULES as OJA_MODULES
from src.applications.ojadoctor.modules import MODULES as DOCTOR_MODULES


home_bp = Blueprint(

    "home",

    __name__

)


@home_bp.route("/")
def home():

    applications = {

        "oja": {

            "name": "OJA",

            "modules": list(OJA_MODULES.keys())

        },

        "ojadoctor": {

            "name": "OJA Doctor",

            "modules": list(DOCTOR_MODULES.keys())

        }

    }

    return render_template(

        "index.html",

        applications=applications,

        modules=list(OJA_MODULES.keys())

    )