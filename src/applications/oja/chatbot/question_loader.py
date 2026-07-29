"""
question_loader.py

Loads chatbot questions.
"""

import json
import random
from pathlib import Path

from src.applications.oja.chatbot.config import ChatbotConfig


class QuestionLoader:

    FILE = (
        Path(__file__).resolve().parent
        / "knowledge"
        / "questions.json"
    )

    @classmethod
    def load(cls):

        with open(

            cls.FILE,

            "r",

            encoding="utf-8"

        ) as file:

            questions = json.load(file)

        # Only enabled questions
        questions = [

            question

            for question in questions

            if question.get("enabled", True)

        ]

        # Random Questions
        if QUESTIONS_PER_RUN >= len(questions):

            return questions

        return random.sample(

            questions,

            QUESTIONS_PER_RUN

        )

    @classmethod
    def load_by_priority(

        cls,

        priority

    ):

        with open(

            cls.FILE,

            "r",

            encoding="utf-8"

        ) as file:

            questions = json.load(file)

        questions = [

            question

            for question in questions

            if question.get("enabled", True)

            and question.get(

                "priority",

                "Regression"

            ) == priority

        ]

        if QUESTIONS_PER_RUN >= len(questions):

            return questions

        return random.sample(

            questions,

            QUESTIONS_PER_RUN

        )

    @classmethod
    def load_by_category(

        cls,

        category_key

    ):

        with open(

            cls.FILE,

            "r",

            encoding="utf-8"

        ) as file:

            questions = json.load(file)

        questions = [

            question

            for question in questions

            if question.get("enabled", True)

            and question.get(

                "category_key"

            ) == category_key

        ]

        if QUESTIONS_PER_RUN >= len(questions):

            return questions

        return random.sample(

            questions,

            QUESTIONS_PER_RUN

        )