"""
validator.py

Reusable UI validator.
"""


class Validator:

    def __init__(self, page):

        self.page = page

    # --------------------------------------------------
    # Verify Texts
    # --------------------------------------------------

    def verify_texts(

        self,

        title,

        texts,

        exact=True,

        timeout=10000

    ):

        print(f"\nVerifying {title}...")

        for text in texts:

            self.page.get_by_text(

                text,

                exact=exact

            ).first.wait_for(

                state="visible",

                timeout=timeout

            )

            print(f"✓ {text}")

        return True

    # --------------------------------------------------
    # Verify Locator Exists
    # --------------------------------------------------

    def verify_locator(

        self,

        locator,

        title="Locator",

        timeout=10000

    ):

        print(f"\nVerifying {title}...")

        locator.wait_for(

            state="visible",

            timeout=timeout

        )

        print(f"✓ {title}")

        return True

    # --------------------------------------------------
    # Verify Page Title
    # --------------------------------------------------

    def verify_title(

        self,

        locators

    ):

        for selector in locators:

            try:

                element = self.page.locator(

                    selector

                )

                if element.count() == 0:

                    continue

                text = element.first.inner_text().strip()

                if text:

                    print(f"✓ Title : {text}")

                    return True

            except Exception:

                continue

        print("✗ Title not found.")

        return False

    # --------------------------------------------------
    # Verify Body
    # --------------------------------------------------

    def verify_body(

        self,

        locators

    ):

        for selector in locators:

            try:

                body = self.page.locator(

                    selector

                )

                if body.count() > 0:

                    print("✓ Body Found")

                    return True

            except Exception:

                continue

        print("✗ Body not found.")

        return False

    # --------------------------------------------------
    # Verify Empty State
    # --------------------------------------------------

    def verify_empty_state(

        self,

        locators

    ):

        for selector in locators:

            try:

                empty = self.page.locator(

                    selector

                )

                if empty.count() > 0:

                    print("✓ Empty State")

                    return True

            except Exception:

                continue

        return False