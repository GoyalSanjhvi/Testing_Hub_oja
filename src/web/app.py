from flask import Flask

from src.web.routes.home import home_bp
from src.web.routes.execution import execution_bp

app = Flask(__name__)

app.register_blueprint(home_bp)

app.register_blueprint(execution_bp)


if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )