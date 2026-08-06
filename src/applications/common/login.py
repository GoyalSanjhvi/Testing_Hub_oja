"""
login.py

Logs into Oja Fertility.
"""

from src.applications.common.config import Config
from src.framework.evidence import Evidence


class Login:

    def __init__(

        self,

        page,

        application="oja",

        account="patient"

    ):

        self.page = page

        self.application = application

        self.account = account

        credentials = Config.get_account(

            account

        )

        self.email = credentials["email"]

        self.password = credentials["password"]

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

        Evidence.step(

            page=self.page,

            application=self.application,

            module="Login",

            title="Login Page Opened"

        )

    # --------------------------------------------------
    # Email
    # --------------------------------------------------

    def enter_email(self):

        print("\nEntering Email...")

        email = self.page.get_by_role(

            "textbox",

            name="you@example.com or 98765"

        )

        email.wait_for(

            state="visible",

            timeout=15000

        )

        email.fill(

            self.email

        )

        print("Email Entered.")

        Evidence.step(

            page=self.page,

            application=self.application,

            module="Login",

            title="Email Entered"

        )

    # --------------------------------------------------
    # Continue
    # --------------------------------------------------

    def continue_login(self):

        print("Clicking Enter...")

        button = self.page.get_by_role(

            "button",

            name="Enter"

        )

        button.wait_for(

            state="visible",

            timeout=15000

        )

        button.click()

        self.page.wait_for_load_state(

            "networkidle"

        )

        print("Enter Clicked.")

        Evidence.step(

            page=self.page,

            application=self.application,

            module="Login",

            title="Password Screen Opened"

        )

    # --------------------------------------------------
    # Password
    # --------------------------------------------------

    def enter_password(self):

        print("Waiting for Password Screen...")

        password = self.page.get_by_role(

            "textbox",

            name="Enter your password"

        )

        password.wait_for(

            state="visible",

            timeout=15000

        )

        password.fill(

            self.password

        )

        print("Password Entered.")

        Evidence.step(

            page=self.page,

            application=self.application,

            module="Login",

            title="Password Entered"

        )

    # --------------------------------------------------
    # Login
    # --------------------------------------------------

    def submit(self):

        print("Clicking Login...")

        button = self.page.get_by_role(

            "button",

            name="Login"

        )

        button.wait_for(

            state="visible",

            timeout=15000

        )

        button.click()

        print("Login Clicked.")

    # --------------------------------------------------
    # Verify
    # --------------------------------------------------

    def verify(self):

        self.page.wait_for_load_state(

            "networkidle"

        )

        self.page.wait_for_timeout(

            2000

        )

        success = (

            "dashboard"

            in

            self.page.url.lower()

        )

        Evidence.step(

            page=self.page,

            application=self.application,

            module="Login",

            title="Dashboard Loaded" if success else "Login Failed",

            status="PASS" if success else "FAIL"

        )

        return success

    # --------------------------------------------------
    # Execute
    # --------------------------------------------------

    def execute(self):

        try:

            Evidence.clear(

                self.application,

                "Login"

            )

            self.open()

            self.enter_email()

            self.continue_login()

            self.enter_password()

            self.submit()

            return self.verify()

        except Exception as e:

            print(f"Login Error : {e}")

            try:

                Evidence.step(

                    page=self.page,

                    application=self.application,

                    module="Login",

                    title=str(e),

                    status="FAIL"

                )

            except Exception:
                pass

            return False