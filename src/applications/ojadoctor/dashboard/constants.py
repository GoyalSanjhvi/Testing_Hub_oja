"""
constants.py

Doctor Dashboard locators.
"""


class DashboardConstants:

    # --------------------------------------------------
    # Timeouts
    # --------------------------------------------------

    LOAD_TIMEOUT = 15000

    WAIT_TIME = 2000

    # --------------------------------------------------
    # Dashboard Cards
    # --------------------------------------------------

    CARD_LOCATORS = [

        "[data-testid='dashboard-card']",

        ".dashboard-card",

        ".card",

        ".MuiCard-root"

    ]

    # --------------------------------------------------
    # Dashboard Titles
    # --------------------------------------------------

    TITLE_LOCATORS = [

        "h1",

        "h2",

        ".page-title",

        "[data-testid='page-title']"

    ]

    # --------------------------------------------------
    # Dashboard Widgets
    # --------------------------------------------------

    WIDGETS = [

        "Patients Seen",

        "Today's Appointments",

        "Pending Requests",

        "Appointments"

    ]

    # --------------------------------------------------
    # Empty State
    # --------------------------------------------------

    EMPTY_LOCATORS = [

        ".empty-state",

        ".no-data"

    ]