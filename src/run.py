"""
run.py

Entry point for console execution.
"""

from src.framework.browser import Browser
from src.framework.runner import Runner
from src.framework.report import Report

MODE = "visual"


def main():

    browser = Browser(MODE)

    page = browser.open()

    runner = Runner(page)

    report = Report()

    for module in runner.available_modules():

        status, duration = runner.run(module)

        report.add(

            module,

            status,

            duration

        )

    browser.close()

    print()

    for result in report.all():

        print(result)


if __name__ == "__main__":

    main()