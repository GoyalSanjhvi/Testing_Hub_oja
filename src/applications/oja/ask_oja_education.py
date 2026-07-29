"""
ask_oja_education.py

Executes Ask Oja chatbot via Education Hub.
"""

from src.applications.oja.base_navigation import BaseNavigation
from src.applications.oja.chatbot.base_chatbot import BaseChatbot


class AskOjaEducation(
    BaseNavigation,
    BaseChatbot
):

    TAB_NAME = "Education Hub"

    def __init__(self, page):

        BaseNavigation.__init__(self, page)

        BaseChatbot.__init__(self, page)

    def open_chatbot(self):

        print("Opening Ask Oja...")

        ask_oja = self.page.get_by_role(
            "button",
            name="Ask Oja",
            exact=True
        )

        ask_oja.wait_for(
            state="visible",
            timeout=10000
        )

        ask_oja.click()

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

            print(f"Ask Oja Education Error : {e}")

            return False