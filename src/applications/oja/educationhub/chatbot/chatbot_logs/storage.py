"""
storage.py

Handles chatbot log storage.
"""

import json
from pathlib import Path


class ChatbotStorage:

    LOG_FOLDER = (
        Path("src")
        / "outputs"
        / "chatbot_logs"
    )

    @classmethod
    def initialize(cls):
        """
        Create chatbot log directory if it doesn't exist.
        """

        cls.LOG_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

    @classmethod
    def save(cls, filename, data):
        """
        Save a chatbot log as JSON.
        """

        cls.initialize()

        filepath = cls.LOG_FOLDER / filename

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return filepath

    @classmethod
    def load(cls, filename):
        """
        Load a chatbot log.
        """

        filepath = cls.LOG_FOLDER / filename

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @classmethod
    def list_logs(cls):
        """
        Return all chatbot log files (newest first).
        """

        cls.initialize()

        return sorted(
            cls.LOG_FOLDER.glob("*.json"),
            reverse=True
        )

    @classmethod
    def delete(cls, filename):
        """
        Delete a chatbot log.
        """

        filepath = cls.LOG_FOLDER / filename

        if filepath.exists():

            filepath.unlink()

            return True

        return False

    @classmethod
    def delete_all(cls):
        """
        Delete all chatbot logs.
        """

        cls.initialize()

        for file in cls.LOG_FOLDER.glob("*.json"):

            file.unlink()