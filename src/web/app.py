"""
app.py

Flask Web Dashboard
"""

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from src.applications.oja.modules import MODULES

from src.framework.browser import Browser
from src.framework.runner import Runner
from src.framework.output import Output
from src.framework.report import Report


app = Flask(__name__)


# ----------------------------------------------------
# Home
# ----------------------------------------------------

@app.route("/")
def home():

    return render_template(

        "index.html",

        modules=list(MODULES.keys())

    )


# ----------------------------------------------------
# Run Single Module
# ----------------------------------------------------

@app.post("/run")
def run_module():

    data = request.get_json()

    module = data["module"]

    mode = data["mode"]

    # Initialize output/report only for Login
    # (Login is always the first module in Run All)

    if module == "Login":

        Output.start_execution()

        Report.initialize(mode)

    browser = Browser(mode)

    try:

        page = browser.open()

        runner = Runner(

            page,

            mode

        )

        result = runner.run(module)

        return jsonify(result)

    except Exception as e:

        print(e)

        return jsonify({

            "module": module,

            "status": "FAIL",

            "duration": 0

        })

    finally:

        browser.close()


# ----------------------------------------------------
# Main
# ----------------------------------------------------

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )