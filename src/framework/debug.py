"""
debug.py

Debug utility for Playwright automation.
"""

from pathlib import Path


class Debug:

    OUTPUT = Path("src/outputs/debug")

    @classmethod
    def dump(cls, page, name="page"):

        cls.OUTPUT.mkdir(
            parents=True,
            exist_ok=True
        )

        print("\n" + "=" * 80)
        print("DEBUG INFORMATION")
        print("=" * 80)

        # -------------------------------------------------
        # URL
        # -------------------------------------------------

        print(f"\nCurrent URL : {page.url}")

        # -------------------------------------------------
        # Screenshot
        # -------------------------------------------------

        screenshot = cls.OUTPUT / f"{name}.png"

        page.screenshot(
            path=str(screenshot),
            full_page=True
        )

        print(f"\nScreenshot Saved : {screenshot}")

        # -------------------------------------------------
        # HTML
        # -------------------------------------------------

        html = cls.OUTPUT / f"{name}.html"

        with open(
            html,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(page.content())

        print(f"HTML Saved       : {html}")

        # -------------------------------------------------
        # Visible Text
        # -------------------------------------------------

        print("\nVISIBLE PAGE TEXT")
        print("-" * 80)

        try:

            print(
                page.locator("body").inner_text()
            )

        except Exception as e:

            print(e)

        print("-" * 80)

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------

        print("\nBUTTONS FOUND")
        print("-" * 80)

        buttons = page.locator("button")

        try:

            count = buttons.count()

            print(f"Total Buttons : {count}\n")

            for i in range(count):

                try:

                    print(
                        f"{i} : "
                        f"{buttons.nth(i).inner_text()}"
                    )

                except:

                    print(
                        f"{i} : <No Text>"
                    )

        except Exception as e:

            print(e)

        print("-" * 80)

        # -------------------------------------------------
        # Links
        # -------------------------------------------------

        print("\nLINKS FOUND")
        print("-" * 80)

        links = page.locator("a")

        try:

            count = links.count()

            print(f"Total Links : {count}\n")

            for i in range(count):

                try:

                    print(
                        f"{i} : "
                        f"{links.nth(i).inner_text()}"
                    )

                except:

                    print(
                        f"{i} : <No Text>"
                    )

        except Exception as e:

            print(e)

        print("-" * 80)

        # -------------------------------------------------
        # Ask Oja Search
        # -------------------------------------------------

        print("\nSEARCHING FOR 'Ask Oja'")
        print("-" * 80)

        try:

            print(
                "Text Count :",
                page.get_by_text("Ask Oja").count()
            )

        except Exception as e:

            print(e)

        print("=" * 80)