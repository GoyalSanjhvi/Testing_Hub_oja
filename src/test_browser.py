from src.framework.browser import Browser

browser = Browser("visual")

page = browser.open()

page.goto("https://example.com")

print(page.title())

input("Press Enter to close...")

browser.close()