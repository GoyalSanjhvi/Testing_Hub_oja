"""
education_content.py

Education Hub Content Automation.
"""

from src.applications.oja.base_navigation import BaseNavigation

from .content.tabs import Tabs


class EducationContent(BaseNavigation):

    TAB_NAME = "Education Hub"

    def execute(self):

        try:

            print("\n" + "=" * 70)
            print("EDUCATION CONTENT")
            print("=" * 70)

            if not self.login():

                print("Login Failed")

                return False

            self.click_tab()

            print("Education Hub opened successfully.")

            tabs = Tabs(self.page)

            tabs.click_all()

            print("\nEducation Content Passed")

            return True

        except Exception as e:

            print(f"\nEducation Content Error : {e}")

            return False