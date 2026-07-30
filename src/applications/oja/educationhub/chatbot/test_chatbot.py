"""
test_chatbot.py

Standalone backend test for Ask Oja chatbot.
"""

from pathlib import Path

from src.framework.browser import Browser
from src.applications.oja.login import Login


QUESTION = "What is IVF?"


def dump_debug(page):

    output = Path("src/outputs/debug")

    output.mkdir(
        parents=True,
        exist_ok=True
    )

    print("\n" + "=" * 80)
    print("DEBUG INFORMATION")
    print("=" * 80)

    print(f"\nCurrent URL : {page.url}")

    screenshot = output / "education_hub.png"

    page.screenshot(
        path=str(screenshot),
        full_page=True
    )

    print(f"Screenshot Saved : {screenshot}")

    html = output / "education_hub.html"

    with open(
        html,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(page.content())

    print(f"HTML Saved       : {html}")

    print("\n" + "=" * 80)
    print("VISIBLE PAGE TEXT")
    print("=" * 80)

    try:

        print(
            page.locator("body").inner_text()
        )

    except Exception as e:

        print(e)

    print("\n" + "=" * 80)
    print("LOCATOR COUNTS")
    print("=" * 80)

    locators = [

        (
            "Button",
            page.get_by_role(
                "button",
                name="Ask Oja"
            )
        ),

        (
            "Text",
            page.get_by_text(
                "Ask Oja"
            )
        ),

        (
            "Locator(text=Ask Oja)",
            page.locator("text=Ask Oja")
        ),

        (
            "Locator(:has-text)",
            page.locator(":has-text('Ask Oja')")
        )

    ]

    for name, locator in locators:

        try:

            print(f"{name:25} : {locator.count()}")

        except Exception as e:

            print(f"{name:25} : {e}")

    print("\nDebug complete.\n")


def main():

    browser = Browser(
        mode="visual"
    )

    page = browser.open()

    try:

        print("=" * 70)
        print("ASK OJA BACKEND TEST")
        print("=" * 70)

        print("\nLogging in...")

        if not Login(page).execute():

            print("Login Failed")
            return

        print("Login Successful")

        # -------------------------------------------------
        # Open Education Hub
        # -------------------------------------------------

        print("\nOpening Education Hub...")

        education = page.get_by_role(
            "link",
            name="Education Hub",
            exact=True
        )

        education.wait_for(
            state="visible",
            timeout=10000
        )

        education.click()

        page.wait_for_load_state("networkidle")

        page.wait_for_timeout(3000)

        print("Education Hub Opened")

        # -------------------------------------------------
        # Open Ask Oja
        # -------------------------------------------------

        print("\nOpening Ask Oja...")

        education_dropdown = page.locator(
            "button[aria-label='More education pages']"
        )

        education_dropdown.wait_for(
            state="visible",
            timeout=10000
        )

        education_dropdown.click()

        page.wait_for_timeout(1000)

        ask_oja = page.locator(
            "button:has(span:text('Ask Oja'))"
        )

        count = ask_oja.count()

        print(f"Ask Oja Count : {count}")

        if count == 0:

            print("Ask Oja button not found.")

            dump_debug(page)

            input("\nPress ENTER to close...")

            return

        ask_oja.first.wait_for(
            state="visible",
            timeout=10000
        )

        ask_oja.first.click()

        print("Ask Oja Clicked")

        page.wait_for_load_state("networkidle")

        page.wait_for_timeout(5000)

        print(f"Current URL : {page.url}")

        output = Path("src/outputs/debug")

        output.mkdir(
            parents=True,
            exist_ok=True
        )

        page.screenshot(
            path=str(output / "after_click.png"),
            full_page=True
        )

        with open(
            output / "after_click.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(page.content())

        dump_debug(page)

        input("\nPress ENTER to close...")

    except Exception as e:

        print("\n" + "=" * 70)
        print("ERROR")
        print("=" * 70)
        print(e)

    finally:

        browser.close()


if __name__ == "__main__":

    main()