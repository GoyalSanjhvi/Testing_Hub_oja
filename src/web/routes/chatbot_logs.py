"""
chatbot_logs.py

Routes for chatbot execution logs.
"""

from flask import (
    Blueprint,
    jsonify,
    render_template,
    request
)

from src.web.services.chatbot_log_service import (
    ChatbotLogService
)


chatbot_logs_bp = Blueprint(

    "chatbot_logs",

    __name__

)


# ==========================================================
# PAGE
# ==========================================================

@chatbot_logs_bp.route(

    "/chatbot-logs"

)

def chatbot_logs_page():

    return render_template(

        "chatbot_logs.html"

    )


# ==========================================================
# API
# ==========================================================

@chatbot_logs_bp.route(

    "/api/chatbot-logs"

)

def all_logs():

    return jsonify(

        ChatbotLogService.all_logs()

    )


@chatbot_logs_bp.route(

    "/api/chatbot-logs/<filename>"

)

def get_log(filename):

    return jsonify(

        ChatbotLogService.get_log(

            filename

        )

    )


@chatbot_logs_bp.route(

    "/api/chatbot-logs/<filename>",

    methods=["DELETE"]

)

def delete_log(filename):

    return jsonify({

        "success":

        ChatbotLogService.delete_log(

            filename

        )

    })


@chatbot_logs_bp.route(

    "/api/chatbot-logs/delete-selected",

    methods=["POST"]

)

def delete_selected():

    data = request.get_json()

    return jsonify({

        "deleted":

        ChatbotLogService.delete_logs(

            data.get(

                "filenames",

                []

            )

        )

    })


@chatbot_logs_bp.route(

    "/api/chatbot-logs/delete-all",

    methods=["DELETE"]

)

def delete_all():

    ChatbotLogService.delete_all()

    return jsonify({

        "success": True

    })