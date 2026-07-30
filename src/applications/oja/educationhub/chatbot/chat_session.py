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
        status,
        duration=0
    ):

        self.results.append({

            "id": question.get("id"),

            "category": question.get("category"),

            "category_key": question.get("category_key"),

            "question": question.get("question"),

            "priority": question.get("priority"),

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

        print("\n" + "=" * 70)
        print("CHATBOT SUMMARY")
        print("=" * 70)
        print(f"Total Questions : {self.total()}")
        print(f"Passed          : {self.passed()}")
        print(f"Failed          : {self.failed()}")
        print("=" * 70)

        return {
            "total": self.total(),
            "passed": self.passed(),
            "failed": self.failed()
        }

    def all(self):

        return self.results