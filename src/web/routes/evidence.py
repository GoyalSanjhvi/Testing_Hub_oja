"""
evidence.py

Evidence routes.
"""

from pathlib import Path

from flask import Blueprint
from flask import jsonify
from flask import send_file
from flask import abort

from src.web.services.evidence_service import EvidenceService


evidence_bp = Blueprint(

    "evidence",

    __name__

)


# --------------------------------------------------
# Logs
# --------------------------------------------------

@evidence_bp.get(

    "/logs/<application>/<module>"

)
def logs(

    application,

    module

):

    return jsonify(

        EvidenceService.logs(

            application,

            module

        )

    )


# --------------------------------------------------
# Evidence JSON
# --------------------------------------------------

@evidence_bp.get(

    "/evidence/<application>/<module>"

)
def evidence(

    application,

    module

):

    return jsonify(

        EvidenceService.evidence(

            application,

            module

        )

    )


# --------------------------------------------------
# Screenshot
# --------------------------------------------------

@evidence_bp.get(

    "/file/screenshot/<application>/<module>/<filename>"

)
def screenshot(

    application,

    module,

    filename

):

    path = (

        Path("src/outputs/latest")

        / application

        / module

        / filename

    )

    if not path.exists():

        abort(404)

    return send_file(path)


# --------------------------------------------------
# HTML
# --------------------------------------------------

@evidence_bp.get(

    "/file/html/<application>/<module>/<filename>"

)
def html(

    application,

    module,

    filename

):

    path = (

        Path("src/outputs/latest")

        / application

        / module

        / filename

    )

    if not path.exists():

        abort(404)

    return send_file(path)