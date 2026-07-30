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

            self.page.locator("button:has-text('Send')"),

            self.page.locator("button[type='submit']")

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

        print("Send button not found.")

        return None

    def response_locator(self):

        return self.page.locator(
            ".prose, .markdown, p"
        )

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

            value = box.input_value()

            print(f"Textbox Value : {value}")

        except Exception:

            print("Textbox value could not be verified.")

    def send(self):

        print("\nSending Question...")

        button = self.send_button()

        if button:

            try:

                button.click()

                print("Send button clicked.")

                return

            except Exception as e:

                print(f"Button click failed : {e}")

        print("Trying ENTER key...")

        self.question_box().press("Enter")

    def wait_for_response(self):

        print("\nWaiting for AI response...")

        self.page.wait_for_timeout(5000)

    def latest_response(self):

        responses = self.response_locator()

        count = responses.count()

        print(f"Response Elements : {count}")

        if count == 0:

            return ""

        print("\nScanning all response elements...")

        for i in range(count - 1, -1, -1):

            try:

                text = responses.nth(i).inner_text().strip()

                if not text:
                    continue

                print(f"[{i}] {text[:80]}")

                if (
                    len(text) > 20
                    and text.upper() != "SOURCES"
                    and text.upper() != "SOURCE"
                    and text.upper() != "REFERENCES"
                    and "Type your health question" not in text
                ):

                    print("\nAI RESPONSE")
                    print("-" * 40)
                    print(text)
                    print("-" * 40)

                    return text

            except Exception:
                pass

        print("No valid AI response found.")

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

        duration = round(time() - start, 2)

        print(f"Completed in {duration} sec")

        print("=" * 70)

        return response