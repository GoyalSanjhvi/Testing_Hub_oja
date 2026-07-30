"""
ask_oja_education.py

Executes Ask Oja chatbot via Education Hub.
"""

from src.applications.oja.base_navigation import BaseNavigation
from src.applications.oja.educationhub.chatbot.base_chatbot import BaseChatbot


class AskOjaEducation(
    BaseNavigation,
    BaseChatbot
):

    TAB_NAME = "Education Hub"

    def __init__(self, page):

        BaseNavigation.__init__(self, page)
        BaseChatbot.__init__(self, page)

    def open_chatbot(self):

        print("\n" + "=" * 70)
        print("ASK OJA CHATBOT")
        print("=" * 70)

        print("Opening Ask Oja...")

        #
        # Open "More education pages"
        #
        more_pages = self.page.locator(
            "button[aria-label='More education pages']"
        )

        more_pages.wait_for(
            state="visible",
            timeout=10000
        )

        more_pages.click()

        self.page.wait_for_timeout(1000)

        #
        # Click Ask Oja
        #
        ask_oja = self.page.locator(
            "button:has(span:text('Ask Oja'))"
        )

        ask_oja.wait_for(
            state="visible",
            timeout=10000
        )

        ask_oja.click()

        #
        # Wait for chatbot page
        #
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)

        print("Ask Oja opened successfully.")

    def execute(self):

        try:

            if not self.login():

                print("Login Failed")
                return False

            #
            # Open Education Hub
            #
            self.click_tab()

            #
            # Execute chatbot
            #
            return self.execute_chat()

        except Exception as e:

            print(f"Ask Oja Education Error : {e}")

            return False