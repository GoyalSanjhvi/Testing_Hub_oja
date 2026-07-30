"""
question_selector.py

Selects chatbot questions.
"""

import random


class QuestionSelector:

    @staticmethod
    def random(questions, count):

        if count >= len(questions):

            return questions

        return random.sample(

            questions,

            count

        )

    @staticmethod
    def sequential(questions, count):

        return questions[:count]

    @staticmethod
    def by_category(

        questions,

        category_key,

        count

    ):

        filtered = [

            question

            for question in questions

            if question.category_key == category_key

        ]

        return QuestionSelector.random(

            filtered,

            count

        )

    @staticmethod
    def by_priority(

        questions,

        priority,

        count

    ):

        filtered = [

            question

            for question in questions

            if question.priority == priority

        ]

        return QuestionSelector.random(

            filtered,

            count

        )