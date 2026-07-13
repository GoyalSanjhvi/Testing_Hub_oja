"""
platform.py

Handles execution mode.
"""


class Platform:

    def __init__(self, mode="visual"):

        self.mode = mode.lower()

        self.headless = self.mode == "regression"

    def __str__(self):

        return (
            f"\n"
            f"Mode      : {self.mode.upper()}\n"
            f"Headless  : {self.headless}\n"
        )