"""
constants.py

Constants used by the Education Hub content module.
"""


class ContentConstants:

    # Timeouts
    LOAD_TIMEOUT = 10000
    WAIT_TIME = 2000

    # Education Hub Tabs
    TABS = [
        "All Content",
        "Articles",
        "Videos",
        "Infographics",
        "Podcasts",
        "Saved"
    ]

    # Possible content card locators
    CARD_LOCATORS = [
        "[data-testid='content-card']",
        "[data-testid='article-card']",
        ".content-card",
        ".article-card",
        "article",
        "a[href*='article']",
        "a[href*='content']"
    ]

    # Possible title locators on the details page
    TITLE_LOCATORS = [
        "h1",
        "h2",
        "[data-testid='title']",
        ".title"
    ]

    # Body/content locators
    BODY_LOCATORS = [
        ".prose",
        ".markdown",
        "article",
        "main",
        "p"
    ]

    # Empty state locators (especially for Saved tab)
    EMPTY_STATE_LOCATORS = [
        "[data-testid='empty-state']",
        ".empty-state",
        ".no-data",
        ".no-content"
    ]