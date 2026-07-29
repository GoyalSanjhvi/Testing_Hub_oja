"""
chat_session.py

Stores chatbot execution details.
"""


class ChatSession:

    def __init__(self):

        self.results = []

    def add(

        self,

        question,

        response,

        duration,

        status

    ):

        self.results.append({

            "id": question.id,

            "category": question.category,

            "category_key": question.category_key,

            "question": question.question,

            "priority": question.priority,

            "response": response,

            "duration": duration,

            "status": status

        })

    def total(self):

        return len(self.results)

    def passed(self):

        return sum(

            1

            for result in self.results

            if result["status"]

        )

    def failed(self):

        return self.total() - self.passed()

    def success(self):

        return self.failed() == 0

    def summary(self):

        return {

            "total": self.total(),

            "passed": self.passed(),

            "failed": self.failed()

        }

    def all(self):

        return self.results