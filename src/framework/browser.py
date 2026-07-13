"""
browser.py

Creates and manages Playwright browser.
"""

from playwright.sync_api import sync_playwright

from src.framework.platform import Platform


class Browser:

    def __init__(self, mode="visual"):

        self.platform = Platform(mode)

        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def open(self):

        self.playwright = sync_playwright().start()

        print(self.platform)

        self.browser = self.playwright.chromium.launch(

            headless=self.platform.headless,

            slow_mo=300 if not self.platform.headless else 0

        )

        self.context = self.browser.new_context()

        self.page = self.context.new_page()

        return self.page

    def close(self):

        if self.context:
            self.context.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()