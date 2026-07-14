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

    module = data["module"]

    mode = data["mode"]

    result = ExecutionService.run(

        module,

        mode

    )

    return jsonify(result)