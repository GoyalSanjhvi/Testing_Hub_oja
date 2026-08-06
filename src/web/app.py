"""
app.py

Flask application.
"""

from flask import Flask

from src.web.routes.home import home_bp
from src.web.routes.execution import execution_bp
from src.web.routes.evidence import evidence_bp


app = Flask(

    __name__,

    template_folder="templates",

    static_folder="static"

)


# --------------------------------------------------
# Blueprints
# --------------------------------------------------

app.register_blueprint(

    home_bp

)

app.register_blueprint(

    execution_bp

)

app.register_blueprint(

    evidence_bp

)


# --------------------------------------------------
# Run
# --------------------------------------------------

if __name__ == "__main__":

    app.run(

        debug=True

    )