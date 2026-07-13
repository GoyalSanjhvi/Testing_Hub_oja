"""
app.py

Flask Web Dashboard
"""

from flask import Flask, jsonify, render_template, request

from src.applications.oja.modules import MODULES
from src.framework.browser import Browser
from src.framework.runner import Runner

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(

        "index.html",

        modules=list(MODULES.keys())

    )


@app.post("/run")
def run_module():

    data = request.get_json()

    module = data["module"]

    mode = data["mode"]

    browser = Browser(mode)

    try:

        page = browser.open()

        runner = Runner(page)

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


@app.post("/run_all")
def run_all():

    data = request.get_json()

    mode = data["mode"]

    results = []

    for module in MODULES.keys():

        browser = Browser(mode)

        try:

            page = browser.open()

            runner = Runner(page)

            results.append(

                runner.run(module)

            )

        except Exception as e:

            print(e)

            results.append({

                "module": module,

                "status": "FAIL",

                "duration": 0

            })

        finally:

            browser.close()

    return jsonify(results)


if __name__ == "__main__":

    app.run(

        debug=True

    )