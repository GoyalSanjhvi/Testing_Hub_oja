from playwright.sync_api import sync_playwright

from src.applications.ojadoctor.dashboard.dashboard import Dashboard


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    Dashboard(page).execute()

    input("\nPress ENTER to close...")

    browser.close()