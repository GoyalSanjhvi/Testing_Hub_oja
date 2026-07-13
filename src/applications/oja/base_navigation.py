"""
base_navigation.py

Base class for all navigation modules.
"""

from src.applications.oja.login import Login


class BaseNavigation:

    TAB_NAME = ""

    def __init__(self, page):

        self.page = page

    def login(self):

        return Login(self.page).execute()

    def click_tab(self):

        print(f"Opening {self.TAB_NAME}...")

        self.page.wait_for_timeout(1000)

        tab = self.page.get_by_role(
            "link",
            name=self.TAB_NAME,
            exact=True
        )

        tab.wait_for(state="visible", timeout=10000)

        tab.click(force=True)

        self.page.wait_for_timeout(2000)

    def verify(self):

        try:

            print(f"Current URL : {self.page.url}")

            tab = self.page.get_by_role(
                "link",
                name=self.TAB_NAME,
                exact=True
            )

            if tab.get_attribute("aria-current") == "page":

                return True

            if self.TAB_NAME.lower().replace(" ", "") in self.page.url.lower():

                return True

            return False

        except Exception as e:

            print(f"Verification Error : {e}")

            return False

    def execute(self):

        try:

            if not self.login():

                print("Login Failed")

                return False

            self.click_tab()

            return self.verify()

        except Exception as e:

            print(f"{self.TAB_NAME} Error : {e}")

            return False