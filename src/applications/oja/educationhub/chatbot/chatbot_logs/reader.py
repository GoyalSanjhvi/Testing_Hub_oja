"""
reader.py

Reads chatbot execution logs.
"""

from .storage import ChatbotStorage


class ChatbotLogReader:

    @classmethod
    def all_logs(cls):
        """
        Return all chatbot logs (newest first).
        """

        logs = []

        for file in ChatbotStorage.list_logs():

            try:

                data = ChatbotStorage.load(
                    file.name
                )

                data["filename"] = file.name

                logs.append(data)

            except Exception as e:

                print(
                    f"Unable to read {file.name}: {e}"
                )

        return logs

    @classmethod
    def get_log(
        cls,
        filename
    ):
        """
        Return one chatbot log.
        """

        return ChatbotStorage.load(
            filename
        )

    @classmethod
    def total_logs(cls):
        """
        Total number of chatbot logs.
        """

        return len(
            ChatbotStorage.list_logs()
        )

    @classmethod
    def passed_logs(cls):

        return sum(

            1

            for log in cls.all_logs()

            if log["status"] == "PASS"

        )

    @classmethod
    def failed_logs(cls):

        return sum(

            1

            for log in cls.all_logs()

            if log["status"] == "FAIL"

        )