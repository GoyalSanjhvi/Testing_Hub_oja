"""
base_chatbot.py

Reusable chatbot execution flow.
"""

from time import time

from src.applications.oja.educationhub.chatbot.chat_engine import ChatEngine
from src.applications.oja.educationhub.chatbot.chat_session import ChatSession
from src.applications.oja.educationhub.chatbot.question_loader import QuestionLoader
from src.applications.oja.educationhub.chatbot.response_validator import ResponseValidator

from src.applications.oja.educationhub.chatbot.chatbot_logs.logger import ChatbotLogger


class BaseChatbot:

    MODULE_NAME = "Ask Oja"

    def __init__(self, page):

        self.page = page

        self.chat = ChatEngine(page)

        self.session = ChatSession()

    def open_chatbot(self):

        raise NotImplementedError

    def execute_chat(self):

        start = time()

        self.open_chatbot()

        questions = QuestionLoader.load()

        for question in questions:

            response = self.chat.ask(
                question["question"]
            )

            status = ResponseValidator.validate_question(

                question,

                response

            )

            self.session.add(

                question,

                response,

                status

            )

        self.session.summary()

        duration = round(

            time() - start,

            2

        )

        ChatbotLogger.save(

            module=self.MODULE_NAME,

            session=self.session,

            duration=duration

        )

        return self.session.success()