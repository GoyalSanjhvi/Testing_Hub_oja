"""
base_navigation.py

Base class for all navigation modules.
"""

from src.applications.oja.login import Login


class BaseNavigation:

    TAB_NAME = ""

    # Optional:
    # Override this only if the page URL is different from TAB_NAME.
    URL_KEYWORD = None

    def __init__(self, page):

        self.page = page

    def login(self):

        return Login(self.page).execute()

    def click_tab(self):

        print(f"Opening {self.TAB_NAME}...")

        tab = self.page.get_by_role(
            "link",
            name=self.TAB_NAME,
            exact=True
        )

        tab.wait_for(

            state="visible",

            timeout=15000

        )

        tab.scroll_into_view_if_needed()

        tab.click()

        self.page.wait_for_load_state(

            "networkidle"

        )

    def verify(self):

        try:

            print(f"Current URL : {self.page.url}")

            tab = self.page.get_by_role(
                "link",
                name=self.TAB_NAME,
                exact=True
            )

            # Active navigation tab
            if tab.get_attribute("aria-current") == "page":

                return True

            # URL keyword
            keyword = self.URL_KEYWORD

            if keyword is None:

                keyword = self.TAB_NAME.lower().replace(" ", "")

            if keyword in self.page.url.lower():

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