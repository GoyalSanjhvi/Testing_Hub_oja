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

        print("Searching for question textbox...")

        locators = [

            self.page.get_by_placeholder(
                "Type your health question..."
            ),

            self.page.get_by_role(
                "textbox"
            ),

            self.page.locator("textarea"),

            self.page.locator("input[type='text']"),

            self.page.locator("input")

        ]

        for locator in locators:

            try:

                locator.first.wait_for(
                    state="visible",
                    timeout=2000
                )

                print("Textbox Found")

                return locator.first

            except Exception:

                pass

        raise Exception("Question textbox not found.")

    def send_button(self):

        print("Searching for Send button...")

        locators = [

            self.page.get_by_role(
                "button",
                name="Send"
            ),

            self.page.locator(
                "button:has-text('Send')"
            ),

            self.page.locator(
                "button[type='button']"
            )

        ]

        for locator in locators:

            try:

                locator.first.wait_for(
                    state="visible",
                    timeout=2000
                )

                print("Send Button Found")

                return locator.first

            except Exception:

                pass

        return None

    # --------------------------------------------------
    # Actions
    # --------------------------------------------------

    def type_question(self, question):

        print("\nTyping Question:")
        print(question)

        box = self.question_box()

        box.click()

        box.fill("")

        box.fill(question)

        try:

            print(
                "Textbox Value :",
                box.input_value()
            )

        except Exception:

            pass

    def send(self):

        print("\nSending Question...")

        button = self.send_button()

        if button:

            try:

                button.click()

                print("Send button clicked.")

                return

            except Exception:

                pass

        self.question_box().press("Enter")

    def wait_for_response(self):

        print("\nWaiting for AI response...")

        self.page.wait_for_timeout(5000)

    # --------------------------------------------------
    # AI RESPONSE
    # --------------------------------------------------

    def latest_response(self):

        print("\nSearching latest AI response...")

        locator = self.page.locator(
            "div.max-w-\\[70\\%\\].items-start > div > p"
        )

        count = locator.count()

        print(f"AI Responses Found : {count}")

        if count == 0:

            print("No AI response found.")

            return ""

        for i in range(count - 1, -1, -1):

            try:

                response = locator.nth(i).inner_text().strip()

                if not response:

                    continue

                if len(response) < 20:

                    continue

                print("\n==============================")
                print(f"Response {i}")
                print("==============================")
                print(response)

                return response

            except Exception:

                continue

        return ""

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def ask(self, question):

        print("\n" + "=" * 70)
        print("CHAT ENGINE")
        print("=" * 70)

        print(f"\nAsking: {question}")

        start = time()

        print("[1] Type Question")
        self.type_question(question)

        print("[2] Question Typed")

        print("[3] Sending")
        self.send()

        print("[4] Sent")

        print("[5] Waiting Response")
        self.wait_for_response()

        print("[6] Response Finished")

        response = self.latest_response()

        print("[7] Response Collected")

        duration = round(
            time() - start,
            2
        )

        print(f"Completed in {duration} sec")

        print("=" * 70)

        return response