"""
locator_debug.py

Utility for discovering Playwright locators.
"""

from pathlib import Path


class LocatorDebug:

    OUTPUT_DIR = Path("src/outputs/debug")

    @classmethod
    def inspect(cls, page):

        cls.OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        # ---------------------------------------------
        # Save HTML
        # ---------------------------------------------

        html_file = cls.OUTPUT_DIR / "page.html"

        html_file.write_text(
            page.content(),
            encoding="utf-8"
        )

        print(f"\nHTML Saved : {html_file}")

        # ---------------------------------------------
        # Save Screenshot
        # ---------------------------------------------

        screenshot = cls.OUTPUT_DIR / "page.png"

        page.screenshot(
            path=str(screenshot),
            full_page=True
        )

        print(f"Screenshot Saved : {screenshot}")

        # ---------------------------------------------
        # Existing Locator Inspector
        # ---------------------------------------------

        print("\n" + "=" * 100)
        print("LOCATOR DEBUG")
        print("=" * 100)

        selectors = [

            ("Tabs", "[role='tab']"),

            ("Buttons", "button"),

            ("Links", "a"),

            ("Role Buttons", "[role='button']"),

            ("Divs", "div"),

            ("Spans", "span"),

            ("Inputs", "input"),

            ("Textareas", "textarea")

        ]

        for title, selector in selectors:

            print("\n" + "=" * 100)
            print(title.upper())
            print("=" * 100)

            elements = page.locator(selector)

            try:

                count = elements.count()

                print(f"Selector : {selector}")
                print(f"Elements : {count}\n")

                for i in range(count):

                    try:

                        element = elements.nth(i)

                        text = element.inner_text().strip()

                        if not text:
                            continue

                        role = element.get_attribute("role")
                        data_testid = element.get_attribute("data-testid")
                        aria_label = element.get_attribute("aria-label")
                        cls_name = element.get_attribute("class")
                        element_id = element.get_attribute("id")

                        print("-" * 100)

                        print(f"Index      : {i}")
                        print(f"Text       : {text}")
                        print(f"Role       : {role}")
                        print(f"Id         : {element_id}")
                        print(f"Class      : {cls_name}")
                        print(f"Aria Label : {aria_label}")
                        print(f"DataTestId : {data_testid}")

                    except Exception:

                        continue

            except Exception:

                pass

        print("\n" + "=" * 100)
        print("END OF LOCATOR DEBUG")
        print("=" * 100)