"""
deleter.py

Deletes chatbot execution logs.
"""

from .storage import ChatbotStorage


class ChatbotLogDeleter:

    @classmethod
    def delete_log(
        cls,
        filename
    ):
        """
        Delete a single chatbot log.
        """

        success = ChatbotStorage.delete(
            filename
        )

        if success:

            print(
                f"Deleted log : {filename}"
            )

        else:

            print(
                f"Log not found : {filename}"
            )

        return success

    @classmethod
    def delete_logs(
        cls,
        filenames
    ):
        """
        Delete multiple chatbot logs.
        """

        deleted = 0

        for filename in filenames:

            if ChatbotStorage.delete(
                filename
            ):

                deleted += 1

        print(
            f"Deleted {deleted} log(s)."
        )

        return deleted

    @classmethod
    def delete_all(cls):
        """
        Delete all chatbot logs.
        """

        ChatbotStorage.delete_all()

        print(
            "All chatbot logs deleted."
        )

        return True