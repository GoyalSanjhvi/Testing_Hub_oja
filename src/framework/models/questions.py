"""
question.py

Represents a chatbot question.
"""


class Question:

    def __init__(
        self,
        question_id,
        category,
        category_key,
        question,
        priority,
        enabled,
        expected_keywords,
        tags
    ):

        self.id = question_id
        self.category = category
        self.category_key = category_key
        self.question = question
        self.priority = priority
        self.enabled = enabled
        self.expected_keywords = expected_keywords
        self.tags = tags

    def to_dict(self):

        return {

            "id": self.id,

            "category": self.category,

            "category_key": self.category_key,

            "question": self.question,

            "priority": self.priority,

            "enabled": self.enabled,

            "expected_keywords": self.expected_keywords,

            "tags": self.tags

        }