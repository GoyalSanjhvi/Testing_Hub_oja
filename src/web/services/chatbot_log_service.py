"""
chatbot_log_service.py

Service layer for chatbot logs.
"""

from src.applications.oja.educationhub.chatbot.chatbot_logs.reader import (
    ChatbotLogReader
)

from src.applications.oja.educationhub.chatbot.chatbot_logs.deleter import (
    ChatbotLogDeleter
)


class ChatbotLogService:

    @staticmethod
    def all_logs():

        return ChatbotLogReader.all_logs()

    @staticmethod
    def get_log(filename):

        return ChatbotLogReader.get_log(
            filename
        )

    @staticmethod
    def delete_log(filename):

        return ChatbotLogDeleter.delete_log(
            filename
        )

    @staticmethod
    def delete_logs(filenames):

        return ChatbotLogDeleter.delete_logs(
            filenames
        )

    @staticmethod
    def delete_all():

        return ChatbotLogDeleter.delete_all()