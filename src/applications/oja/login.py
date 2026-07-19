"""
login.py

Logs into Oja Fertility.
"""

from src.applications.oja.config import Config


class Login:

    def __init__(self, page):

        self.page = page

    def open(self):

        self.page.goto(

            Config.BASE_URL,

            wait_until="domcontentloaded"

        )

        self.page.wait_for_load_state("networkidle")

    def credentials(self):

        email = self.page.get_by_role(

            "textbox",

            name="you@example.com or 98765"

        )

        password = self.page.get_by_role(

            "textbox",

            name="Enter your password"

        )

        email.wait_for(state="visible", timeout=15000)

        password.wait_for(state="visible", timeout=15000)

        email.fill(Config.EMAIL)

        password.fill(Config.PASSWORD)

    def submit(self):

        button = self.page.get_by_role(

            "button",

            name="Login"

        )

        button.wait_for(state="visible", timeout=15000)

        button.click()

    def verify(self):

        self.page.wait_for_load_state("networkidle")

        self.page.wait_for_timeout(1000)

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