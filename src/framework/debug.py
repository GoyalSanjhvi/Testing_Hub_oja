"""
locator_debug.py

Utility for discovering Playwright locators.
"""


class LocatorDebug:

    @classmethod
    def inspect(cls, page):

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

                        print("\nSuggested Locators")

                        print(
                            f'page.get_by_text("{text}", exact=True)'
                        )

                        if selector == "button":

                            print(
                                f'page.locator("button").filter(has_text="{text}")'
                            )

                        if selector == "a":

                            print(
                                f'page.locator("a").filter(has_text="{text}")'
                            )

                        if role:

                            print(
                                f'page.get_by_role("{role}", name="{text}")'
                            )

                        if data_testid:

                            print(
                                f'page.locator("[data-testid=\\"{data_testid}\\"]")'
                            )

                        if element_id:

                            print(
                                f'page.locator("#{element_id}")'
                            )

                    except Exception:
                        continue

            except Exception as e:

                print(e)

        print("\n" + "=" * 100)
        print("END OF LOCATOR DEBUG")
        print("=" * 100)