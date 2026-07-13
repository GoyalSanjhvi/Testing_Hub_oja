"""
login.py

Logs into Oja Fertility.
"""

from src.applications.oja.config import Config


class Login:

    def __init__(self, page):

        self.page = page

    def open(self):

        self.page.goto(Config.BASE_URL)

    def credentials(self):

        self.page.get_by_role(
            "textbox",
            name="you@example.com or 98765"
        ).fill(Config.EMAIL)

        self.page.get_by_role(
            "textbox",
            name="Enter your password"
        ).fill(Config.PASSWORD)

    def submit(self):

        self.page.get_by_role(
            "button",
            name="Login"
        ).click()

    def verify(self):

        self.page.wait_for_load_state("networkidle")

        return "dashboard" in self.page.url.lower()

    def execute(self):

        try:

            self.open()

            self.credentials()

            self.submit()

            return self.verify()

        except Exception as e:

            print(f"Login Error : {e}")

            return False