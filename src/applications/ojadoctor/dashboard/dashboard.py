"""
dashboard.py

Doctor Dashboard Automation.
"""

from src.applications.common.base_navigation import BaseNavigation
from src.applications.common.validator import Validator
from src.applications.common.navigation import Navigation


class Dashboard(BaseNavigation):

    ACCOUNT = "doctor"

    TAB_NAME = "Dashboard"

    URL_KEYWORD = "dashboard"

    def execute(self):

        try:

            print("\n" + "=" * 70)
            print("DOCTOR DASHBOARD")
            print("=" * 70)

            # --------------------------------------------------
            # Login
            # --------------------------------------------------

            if not self.login():

                print("Login Failed")

                return False

            print("✓ Login")

            # --------------------------------------------------
            # Verify Dashboard
            # --------------------------------------------------

            if not self.verify():

                print("Dashboard Verification Failed")

                return False

            print("✓ Dashboard")

            navigation = Navigation(

                self.page

            )

            validator = Validator(

                self.page

            )

            # --------------------------------------------------
            # Navigation
            # --------------------------------------------------

            navigation.verify(

                [

                    "Dashboard",

                    "Patients",

                    "Consultations",

                    "Scheduler",

                    "Prescriptions"

                ]

            )

            # --------------------------------------------------
            # Welcome Section
            # --------------------------------------------------

            validator.verify_texts(

                "Welcome Section",

                [

                    "Welcome back"

                ],

                exact=False

            )

            # --------------------------------------------------
            # Statistics
            # --------------------------------------------------

            validator.verify_texts(

                "Statistics",

                [

                    "Patients Seen",

                    "Today's Appointments",

                    "Pending Requests"

                ]

            )

            # --------------------------------------------------
            # Dashboard Sections
            # --------------------------------------------------

            validator.verify_texts(

                "Dashboard Sections",

                [

                    "Appointments",

                    "Schedule Overview",

                    "Business Metrics",

                    "Patient Monitoring"

                ]

            )

            # --------------------------------------------------
            # Floating Actions
            # --------------------------------------------------

            validator.verify_texts(

                "Floating Actions",

                [

                    "Quick Actions"

                ]

            )

            print("\n" + "=" * 70)
            print("DOCTOR DASHBOARD PASSED")
            print("=" * 70)

            return True

        except Exception as e:

            print(f"\nDashboard Error : {e}")

            return False