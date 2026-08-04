"""
cards.py

Reusable card operations.
"""


class Cards:

    def __init__(

        self,

        page,

        locators,

        wait_time=2000

    ):

        self.page = page

        self.locators = locators

        self.wait_time = wait_time

    # --------------------------------------------------
    # Cards
    # --------------------------------------------------

    def cards(self):

        for locator in self.locators:

            try:

                cards = self.page.locator(

                    locator

                )

                if cards.count() > 0:

                    return cards

            except Exception:

                continue

        return None

    # --------------------------------------------------
    # Count
    # --------------------------------------------------

    def count(self):

        cards = self.cards()

        if cards is None:

            return 0

        return cards.count()

    # --------------------------------------------------
    # Card
    # --------------------------------------------------

    def card(

        self,

        index

    ):

        cards = self.cards()

        if cards is None:

            raise Exception(

                "No cards found."

            )

        if index >= cards.count():

            raise IndexError(

                "Card index out of range."

            )

        return cards.nth(index)

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    def title(

        self,

        index

    ):

        try:

            text = self.card(

                index

            ).inner_text().strip()

            if text:

                return text.split("\n")[0]

        except Exception:

            pass

        return f"Card {index+1}"

    # --------------------------------------------------
    # Open
    # --------------------------------------------------

    def open(

        self,

        index

    ):

        title = self.title(

            index

        )

        print(

            f"\nOpening Card {index+1}: {title}"

        )

        card = self.card(

            index

        )

        card.scroll_into_view_if_needed()

        card.click()

        self.page.wait_for_load_state(

            "networkidle"

        )

        self.page.wait_for_timeout(

            self.wait_time

        )

    # --------------------------------------------------
    # Back
    # --------------------------------------------------

    def back(self):

        print(

            "Returning..."

        )

        self.page.go_back()

        self.page.wait_for_load_state(

            "networkidle"

        )

        self.page.wait_for_timeout(

            self.wait_time

        )

    # --------------------------------------------------
    # Open All
    # --------------------------------------------------

    def open_all(self):

        total = self.count()

        print(

            f"\nTotal Cards : {total}"

        )

        for index in range(total):

            self.open(

                index

            )

            self.back()