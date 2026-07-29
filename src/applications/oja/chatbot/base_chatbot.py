"""
base_chatbot.py

Base class for chatbot execution.
"""

from time import time

from src.applications.oja.chatbot.chat_engine import ChatEngine
from src.applications.oja.chatbot.chat_session import ChatSession
from src.applications.oja.chatbot.question_loader import QuestionLoader
from src.applications.oja.chatbot.response_validator import ResponseValidator


class BaseChatbot:

    def __init__(self, page):

        self.page = page

        self.chat = ChatEngine(page)

        self.session = ChatSession()

    def open_chatbot(self):
        """
        Override in child class.
        """
        raise NotImplementedError

    def execute_chat(self):

        print("\n" + "=" * 70)
        print("ASK OJA CHATBOT")
        print("=" * 70)

        self.open_chatbot()

        questions = QuestionLoader.load()

        print(f"\nQuestions Selected : {len(questions)}\n")

        for question in questions:

            print("-" * 70)

            print(f"Category : {question['category']}")

            print(f"Question : {question['question']}")

            start = time()

            response = self.chat.ask(

                question["question"]

            )

            duration = round(

                time() - start,

                2

            )

            status = ResponseValidator.validate_question(

                question,

                response

            )

            self.session.add(

                question=question,

                response=response,

                duration=duration,

                status=status

            )

            print(f"Status : {'PASS' if status else 'FAIL'}")

            print(f"Time   : {duration} sec")

            print("-" * 70)

        summary = self.session.summary()

        print("\n" + "=" * 70)

        print("CHATBOT SUMMARY")

        print("=" * 70)

        print(f"Questions : {summary['total']}")

        print(f"Passed    : {summary['passed']}")

        print(f"Failed    : {summary['failed']}")

        print("=" * 70)

        return self.session.success()