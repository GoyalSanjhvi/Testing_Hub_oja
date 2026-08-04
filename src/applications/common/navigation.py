"""
navigation.py

Reusable navigation helper.
"""


class Navigation:

    def __init__(
        self,
        page,
        timeout=10000,
        wait_time=2000
    ):

        self.page = page
        self.timeout = timeout
        self.wait_time = wait_time

    # --------------------------------------------------
    # Find Item
    # --------------------------------------------------

    def item(
        self,
        name,
        role=None
    ):

        locators = []

        if role == "button":

            locators.append(

                self.page.get_by_role(

                    "button",

                    name=name,

                    exact=True

                )

            )

        elif role == "link":

            locators.append(

                self.page.get_by_role(

                    "link",

                    name=name,

                    exact=True

                )

            )

        else:

            locators.extend([

                self.page.get_by_role(

                    "button",

                    name=name,

                    exact=True

                ),

                self.page.get_by_role(

                    "link",

                    name=name,

                    exact=True

                ),

                self.page.get_by_text(

                    name,

                    exact=True

                )

            ])

        for locator in locators:

            try:

                locator.first.wait_for(

                    state="visible",

                    timeout=2000

                )

                return locator.first

            except Exception:

                pass

        raise Exception(

            f"{name} not found."

        )

    # --------------------------------------------------
    # Click
    # --------------------------------------------------

    def click(
        self,
        name,
        role=None
    ):

        print("\n" + "=" * 60)
        print(f"Opening : {name}")
        print("=" * 60)

        item = self.item(

            name,

            role

        )

        item.scroll_into_view_if_needed()

        item.click()

        self.page.wait_for_load_state(

            "networkidle"

        )

        self.page.wait_for_timeout(

            self.wait_time

        )

        print(f"✓ {name}")

    # --------------------------------------------------
    # Click All
    # --------------------------------------------------

    def click_all(
        self,
        items,
        role=None
    ):

        for item in items:

            self.click(

                item,

                role

            )

        print("\n✓ Navigation Complete")

    # --------------------------------------------------
    # Verify
    # --------------------------------------------------

    def verify(
        self,
        items,
        role=None
    ):

        print("\nVerifying Navigation...")

        for item in items:

            self.item(

                item,

                role

            )

            print(f"✓ {item}")

        return True