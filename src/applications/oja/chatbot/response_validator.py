"""
response_validator.py

Validates Ask Oja chatbot responses.
"""


class ResponseValidator:

    MIN_RESPONSE_LENGTH = 20

    INVALID_RESPONSES = [

        "",

        "Something went wrong",

        "Error",

        "Try again",

        "Network Error",

        "No response"

    ]

    @classmethod
    def validate(

        cls,

        response

    ):

        if response is None:

            return False

        response = response.strip()

        if response in cls.INVALID_RESPONSES:

            return False

        if len(response) < cls.MIN_RESPONSE_LENGTH:

            return False

        return True

    @classmethod
    def contains_keywords(

        cls,

        response,

        keywords

    ):

        if not keywords:

            return True

        response = response.lower()

        return any(

            keyword.lower() in response

            for keyword in keywords

        )

    @classmethod
    def validate_question(

        cls,

        question,

        response

    ):

        if not cls.validate(response):

            return False

        if not cls.contains_keywords(

            response,

            question.get(

                "expected_keywords",

                []

            )

        ):

            return False

        return True