"""
ask_oja_floating.py

Executes Ask Oja chatbot via Floating Chat.
"""

from src.applications.oja.base_navigation import BaseNavigation
from src.applications.oja.educationhub.chatbot.base_chatbot import BaseChatbot


class AskOjaFloating(
    BaseNavigation,
    BaseChatbot
):

    TAB_NAME = "Dashboard"
    MODULE_NAME = "Ask Oja (Floating)"

    def __init__(self, page):

        BaseNavigation.__init__(self, page)

        BaseChatbot.__init__(self, page)

    def open_chatbot(self):

        print("Opening Floating Ask Oja...")

        floating_chat = self.page.locator(
            "button"
        ).filter(
            has=self.page.locator("svg")
        ).last

        floating_chat.wait_for(
            state="visible",
            timeout=10000
        )

        floating_chat.click()

        self.page.wait_for_load_state(
            "networkidle"
        )

        self.page.wait_for_timeout(2000)

    def execute(self):

        try:

            if not self.login():

                print("Login Failed")

                return False

            self.click_tab()

            return self.execute_chat()

        except Exception as e:

            print(f"Ask Oja Floating Error : {e}")

            return False