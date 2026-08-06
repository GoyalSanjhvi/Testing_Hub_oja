"""
validator.py

Reusable validator.
"""

from src.framework.evidence import Evidence


class Validator:

    def __init__(

        self,

        page,

        module

    ):

        self.page = page

        self.module = module

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

            locator = self.page.get_by_text(

                text,

                exact=exact

            ).first

            locator.wait_for(

                state="visible",

                timeout=timeout

            )

            print(f"✓ {text}")

        Evidence.step(

            page=self.page,

            module=self.module,

            title=title,

            status="PASS"

        )

        return True

    # --------------------------------------------------
    # Verify Locator
    # --------------------------------------------------

    def verify_locator(

        self,

        locator,

        title,

        timeout=10000

    ):

        locator.wait_for(

            state="visible",

            timeout=timeout

        )

        Evidence.step(

            page=self.page,

            module=self.module,

            title=title,

            status="PASS"

        )

        return True