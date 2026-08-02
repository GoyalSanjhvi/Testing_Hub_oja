"""
app.py

Main Flask application.
"""

from flask import Flask

from src.web.routes.home import home_bp
from src.web.routes.execution import execution_bp
from src.web.routes.chatbot_logs import chatbot_logs_bp


app = Flask(__name__)

app.register_blueprint(home_bp)

app.register_blueprint(execution_bp)

app.register_blueprint(chatbot_logs_bp)


if __name__ == "__main__":

    app.run(

        debug=True

    )