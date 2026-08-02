"""
validator.py

Education Hub content validation.
"""

from .constants import ContentConstants


class Validator:

    def __init__(self, page):
        self.page = page

    def verify_title(self):
        """
        Verify content title exists.
        """

        for locator in ContentConstants.TITLE_LOCATORS:

            try:
                title = self.page.locator(locator)

                if title.count() > 0:

                    text = title.first.inner_text().strip()

                    if text:
                        print(f"✓ Title : {text}")
                        return True

            except Exception:
                continue

        print("✗ Title not found.")
        return False

    def verify_body(self):
        """
        Verify content body exists.
        """

        for locator in ContentConstants.BODY_LOCATORS:

            try:
                body = self.page.locator(locator)

                if body.count() > 0:
                    print("✓ Body found.")
                    return True

            except Exception:
                continue

        print("✗ Body not found.")
        return False

    def verify_empty_state(self):
        """
        Verify empty state (e.g. Saved tab with no content).
        """

        for locator in ContentConstants.EMPTY_STATE_LOCATORS:

            try:
                empty = self.page.locator(locator)

                if empty.count() > 0:
                    print("✓ Empty State Found")
                    return True

            except Exception:
                continue

        return False

    def verify_page(self):
        """
        Verify the opened content page.
        """

        print("\nVerifying content page...")

        if self.verify_empty_state():
            print("✓ Empty page verified.")
            return True

        if not self.verify_title():
            raise Exception("Content title not found.")

        if not self.verify_body():
            raise Exception("Content body not found.")

        print("✓ Content verified successfully.")

        return True