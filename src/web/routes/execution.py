"""
execution.py

Execution routes.
"""

from flask import Blueprint
from flask import jsonify
from flask import request

from src.web.services.execution_service import ExecutionService


execution_bp = Blueprint(

    "execution",

    __name__

)


@execution_bp.post("/run")
def run_module():

    data = request.get_json()

    application = data.get(

        "application",

        "oja"

    )

    module = data["module"]

    mode = data["mode"]

    result = ExecutionService.run(

        application=application,

        module=module,

        mode=mode

    )

    return jsonify(result)