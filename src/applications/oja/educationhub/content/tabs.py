"""
tabs.py

Education Hub tab navigation.
"""

from .constants import ContentConstants


class Tabs:

    def __init__(self, page):

        self.page = page

    def click(self, name):

        print("\n" + "=" * 60)
        print(f"Opening Tab : {name}")
        print("=" * 60)

        button = self.page.locator(
            f"button:has-text('{name}')"
        ).first

        button.wait_for(
            state="visible",
            timeout=ContentConstants.LOAD_TIMEOUT
        )

        button.scroll_into_view_if_needed()

        button.click()

        self.page.wait_for_load_state("networkidle")

        self.page.wait_for_timeout(
            ContentConstants.WAIT_TIME
        )

        print(f"{name} opened successfully.")

    def click_all(self):

        for tab in ContentConstants.TABS:

            self.click(tab)

        print("\nAll tabs opened successfully.")