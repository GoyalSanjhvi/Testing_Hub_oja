"""
question_loader.py

Loads chatbot questions.
"""

import json
import random
from pathlib import Path

from src.applications.oja.educationhub.chatbot.config import ChatbotConfig


class QuestionLoader:

    FILE = (
        Path(__file__).resolve().parent
        / "knowledge"
        / "questions.json"
    )

    @classmethod
    def _load_file(cls):
        """Load all questions from JSON file."""

        with open(
            cls.FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @classmethod
    def _select_questions(cls, questions):
        """Randomly select questions based on configuration."""

        if not ChatbotConfig.RANDOMIZE:
            return questions[:ChatbotConfig.QUESTIONS_PER_RUN]

        if ChatbotConfig.QUESTIONS_PER_RUN >= len(questions):
            return questions

        return random.sample(
            questions,
            ChatbotConfig.QUESTIONS_PER_RUN
        )

    @classmethod
    def load(cls):
        """Load all enabled questions."""

        questions = cls._load_file()

        questions = [

            question

            for question in questions

            if question.get("enabled", True)

        ]

        return cls._select_questions(questions)

    @classmethod
    def load_by_priority(
        cls,
        priority
    ):
        """Load enabled questions of a given priority."""

        questions = cls._load_file()

        questions = [

            question

            for question in questions

            if (
                question.get("enabled", True)
                and question.get(
                    "priority",
                    "Regression"
                ) == priority
            )

        ]

        return cls._select_questions(questions)

    @classmethod
    def load_by_category(
        cls,
        category_key
    ):
        """Load enabled questions of a given category."""

        questions = cls._load_file()

        questions = [

            question

            for question in questions

            if (
                question.get("enabled", True)
                and question.get("category_key") == category_key
            )

        ]

        return cls._select_questions(questions)