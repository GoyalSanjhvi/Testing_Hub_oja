"""
logger.py

Creates chatbot execution logs.
"""

from datetime import datetime

from .models import ChatbotLog
from .storage import ChatbotStorage


class ChatbotLogger:

    @classmethod
    def save(
        cls,
        module,
        session,
        duration=0
    ):
        """
        Save one chatbot execution.
        """

        execution_time = datetime.now()

        questions = []

        for item in session.all():

            questions.append({

                "id": item.get("id"),

                "category": item.get("category"),

                "category_key": item.get("category_key"),

                "priority": item.get("priority"),

                "question": item.get("question"),

                "response": item.get("response"),

                "duration": item.get("duration"),

                "status": "PASS" if item.get("status") else "FAIL"

            })

        log = ChatbotLog(

            module=module,

            status=(
                "PASS"
                if session.success()
                else "FAIL"
            ),

            execution_time=execution_time.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            duration=duration,

            questions=questions

        )

        filename = execution_time.strftime(
            "%Y-%m-%d_%H-%M-%S.json"
        )

        ChatbotStorage.save(

            filename,

            log.to_dict()

        )

        print(
            f"\nChatbot log saved : {filename}"
        )

        return filename