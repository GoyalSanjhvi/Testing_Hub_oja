"""
cards.py

Education Hub content card operations.
"""

from .constants import ContentConstants


class Cards:

    def __init__(self, page):
        self.page = page

    def cards(self):
        """
        Return the first locator that matches content cards.
        """

        for locator in ContentConstants.CARD_LOCATORS:

            cards = self.page.locator(locator)

            try:
                if cards.count() > 0:
                    return cards
            except Exception:
                continue

        return None

    def total_cards(self):
        """
        Return total number of cards.
        """

        cards = self.cards()

        if cards is None:
            return 0

        return cards.count()

    def card(self, index):
        """
        Return a specific card.
        """

        cards = self.cards()

        if cards is None:
            raise Exception("No content cards found.")

        if index >= cards.count():
            raise IndexError("Card index out of range.")

        return cards.nth(index)

    def card_title(self, index):
        """
        Return card title.
        """

        card = self.card(index)

        try:
            title = card.inner_text().strip()

            if title:
                return title.split("\n")[0]

        except Exception:
            pass

        return f"Card {index + 1}"

    def open_card(self, index):
        """
        Open a specific card.
        """

        title = self.card_title(index)

        print(f"\nOpening Card {index + 1}: {title}")

        card = self.card(index)

        card.scroll_into_view_if_needed()

        card.click()

        self.page.wait_for_load_state("networkidle")

        self.page.wait_for_timeout(
            ContentConstants.WAIT_TIME
        )

    def back(self):
        """
        Return to the content list.
        """

        print("Returning to content list...")

        self.page.go_back()

        self.page.wait_for_load_state("networkidle")

        self.page.wait_for_timeout(
            ContentConstants.WAIT_TIME
        )

    def open_all_cards(self):
        """
        Open every card one by one.
        """

        total = self.total_cards()

        print(f"\nTotal Cards Found : {total}")

        if total == 0:
            print("No cards found.")
            return

        for index in range(total):

            self.open_card(index)

            self.back()

        print("\nAll cards visited successfully.")