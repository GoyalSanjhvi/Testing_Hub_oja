"""
report.py

Creates and updates automation execution report.
"""

from pathlib import Path
from datetime import datetime


class Report:

    REPORT = Path("src/outputs/latest/report.txt")

    HEADER = (
        "=" * 80 + "\n"
        "                 OJA AUTOMATION EXECUTION REPORT\n"
        + "=" * 80 + "\n\n"
    )

    @classmethod
    def initialize(cls, mode):

        cls.REPORT.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(cls.REPORT, "w", encoding="utf-8") as file:

            file.write(cls.HEADER)

            file.write(
                f"Execution Started : "
                f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            )

            file.write(
                f"Execution Mode    : {mode.upper()}\n\n"
            )

            file.write("-" * 80 + "\n")

            file.write(
                f"{'MODULE':25}"
                f"{'STATUS':15}"
                f"{'TIME'}\n"
            )

            file.write("-" * 80 + "\n")


    @classmethod
    def update(cls,
               module,
               status,
               duration):

        with open(cls.REPORT, "a", encoding="utf-8") as file:

            file.write(
                f"{module:25}"
                f"{status:15}"
                f"{duration:.2f} sec\n"
            )