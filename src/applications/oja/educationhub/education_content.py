"""
education_content.py

Education Hub Content Automation.
"""

from src.applications.common.base_navigation import BaseNavigation
from src.applications.common.navigation import Navigation

from .content.constants import ContentConstants


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

            navigation = Navigation(

                self.page,

                timeout=ContentConstants.LOAD_TIMEOUT,

                wait_time=ContentConstants.WAIT_TIME

            )

            navigation.click_all(

                ContentConstants.TABS,
                role="button"

            )

            print("\nEducation Content Passed")

            return True

        except Exception as e:

            print(f"\nEducation Content Error : {e}")

            return False