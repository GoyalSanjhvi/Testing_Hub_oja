"""
chat_engine.py

Reusable Ask Oja chatbot engine.
"""

from time import time


class ChatEngine:

    RESPONSE_TIMEOUT = 60

    def __init__(self, page):

        self.page = page

    # --------------------------------------------------
    # Locators
    # --------------------------------------------------

    def question_box(self):

        return self.page.get_by_role(
            "textbox",
            name="Type your health question..."
        )

    def send_button(self):

        return self.page.get_by_role(
            "button",
            name="Send"
        )

    def response_locator(self):
        """
        Temporary V1 locator.

        Replace with assistant message locator later.
        """

        return self.page.locator(
            ".prose, .markdown, p"
        )

    # --------------------------------------------------
    # Actions
    # --------------------------------------------------

    def type_question(self, question):

        print(f"Typing : {question}")

        box = self.question_box()

        box.wait_for(state="visible", timeout=10000)

        box.click()

        box.fill(question)

    def send(self):

        print("Sending Question")

        button = self.send_button()

        button.wait_for(state="visible", timeout=10000)

        button.click()

    def wait_for_response(self):

        print("Waiting for AI Response...")

        self.page.wait_for_timeout(5000)

    def latest_response(self):

        responses = self.response_locator()

        count = responses.count()

        if count == 0:

            return ""

        try:

            response = responses.nth(count - 1).inner_text().strip()

            print("\nAI Response:\n")

            print(response)

            print()

            return response

        except Exception:

            return ""

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def ask(self, question):

        print("=" * 60)

        print(f"Asking : {question}")

        start = time()

        self.type_question(question)

        self.send()

        self.wait_for_response()

        response = self.latest_response()

        duration = round(time() - start, 2)

        print(f"Completed in {duration} sec")

        print("=" * 60)

        return response