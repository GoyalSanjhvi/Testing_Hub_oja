"""
login.py

Reusable login for OJA applications.
"""

from src.applications.common.config import Config


class Login:

    def __init__(
        self,
        page,
        account="patient"
    ):

        self.page = page

        self.account = Config.get_account(
            account
        )

    # --------------------------------------------------
    # Open Login Page
    # --------------------------------------------------

    def open(self):

        print("\nOpening Login Page...")

        self.page.goto(

            Config.BASE_URL,

            wait_until="domcontentloaded"

        )

        self.page.wait_for_load_state(
            "networkidle"
        )

    # --------------------------------------------------
    # Email Textbox
    # --------------------------------------------------

    def email_box(self):

        locators = [

            self.page.get_by_role(
                "textbox",
                name="you@example.com or 98765"
            ),

            self.page.get_by_placeholder(
                "you@example.com or 98765 43210"
            ),

            self.page.locator(
                "input[type='email']"
            ),

            self.page.locator(
                "input"
            ).first

        ]

        for locator in locators:

            try:

                locator.first.wait_for(
                    state="visible",
                    timeout=3000
                )

                return locator.first

            except Exception:

                pass

        raise Exception(
            "Email textbox not found."
        )

    # --------------------------------------------------
    # Password Textbox
    # --------------------------------------------------

    def password_box(self):

        locators = [

            self.page.get_by_role(
                "textbox",
                name="Enter your password"
            ),

            self.page.get_by_placeholder(
                "Enter your password"
            ),

            self.page.locator(
                "input[type='password']"
            )

        ]

        for locator in locators:

            try:

                locator.first.wait_for(
                    state="visible",
                    timeout=3000
                )

                return locator.first

            except Exception:

                pass

        raise Exception(
            "Password textbox not found."
        )

    # --------------------------------------------------
    # Enter Email
    # --------------------------------------------------

    def enter_email(self):

        print("\nEntering Email...")

        box = self.email_box()

        box.fill("")

        box.fill(

            self.account["email"]

        )

        print("Email Entered.")

    # --------------------------------------------------
    # Continue
    # --------------------------------------------------

    def continue_login(self):

        print("Clicking Enter...")

        buttons = [

            self.page.get_by_role(
                "button",
                name="Enter"
            ),

            self.page.locator(
                "button:has-text('Enter')"
            )

        ]

        for button in buttons:

            try:

                button.first.wait_for(
                    state="visible",
                    timeout=3000
                )

                button.first.click()

                print("Enter Clicked.")

                return

            except Exception:

                pass

        raise Exception(
            "Enter button not found."
        )

    # --------------------------------------------------
    # Enter Password
    # --------------------------------------------------

    def enter_password(self):

        print("Waiting for Password Screen...")

        self.page.wait_for_load_state(
            "networkidle"
        )

        box = self.password_box()

        box.fill("")

        box.fill(

            self.account["password"]

        )

        print("Password Entered.")

    # --------------------------------------------------
    # Login
    # --------------------------------------------------

    def submit(self):

        print("Clicking Login...")

        buttons = [

            self.page.get_by_role(
                "button",
                name="Login"
            ),

            self.page.locator(
                "button:has-text('Login')"
            )

        ]

        for button in buttons:

            try:

                button.first.wait_for(
                    state="visible",
                    timeout=3000
                )

                button.first.click()

                print("Login Clicked.")

                return

            except Exception:

                pass

        raise Exception(
            "Login button not found."
        )

    # --------------------------------------------------
    # Verify Login
    # --------------------------------------------------

    def verify(self):

        self.page.wait_for_load_state(
            "networkidle"
        )

        self.page.wait_for_timeout(
            Config.WAIT_TIME
        )

        print(
            f"Current URL : {self.page.url}"
        )

        return (

            "dashboard" in self.page.url.lower()

        )

    # --------------------------------------------------
    # Execute Login
    # --------------------------------------------------

    def execute(self):

        try:

            self.open()

            self.enter_email()

            self.continue_login()

            self.enter_password()

            self.submit()

            return self.verify()

        except Exception as e:

            print(
                f"\nLogin Error : {e}"
            )

            return False