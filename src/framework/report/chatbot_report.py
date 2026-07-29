"""
chatbot_report.py

Generates Ask Oja chatbot report.
"""


class ChatbotReport:

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

            "category": question["category"],

            "question": question["question"],

            "response": response,

            "duration": duration,

            "status": status

        })

    def passed(self):

        return sum(

            result["status"]

            for result in self.results

        )

    def failed(self):

        return len(self.results) - self.passed()

    def success(self):

        return self.failed() == 0