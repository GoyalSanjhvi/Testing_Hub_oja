"""
output.py

Manages automation outputs.
"""

import shutil

from pathlib import Path

from datetime import datetime


class Output:

    ROOT = Path("src/outputs")

    LATEST = ROOT / "latest"

    HISTORY = ROOT / "history"


    @classmethod
    def initialize(cls):

        cls.LATEST.mkdir(
            parents=True,
            exist_ok=True
        )

        cls.HISTORY.mkdir(
            parents=True,
            exist_ok=True
        )


    @classmethod
    def archive_latest(cls):

        cls.initialize()

        if not any(cls.LATEST.iterdir()):

            return

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        destination = cls.HISTORY / timestamp

        shutil.copytree(
            cls.LATEST,
            destination
        )

        shutil.rmtree(cls.LATEST)

        cls.LATEST.mkdir()


    @classmethod
    def start_execution(cls):

        cls.archive_latest()


    @classmethod
    def save_error(
        cls,
        module,
        mode,
        duration,
        reason
    ):

        cls.initialize()

        file = cls.LATEST / f"{module}.txt"

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write("="*70+"\n")

            f.write(
                "OJA AUTOMATION FAILURE REPORT\n"
            )

            f.write("="*70+"\n\n")

            f.write(
                f"Module          : {module}\n"
            )

            f.write(
                "Status          : FAIL\n"
            )

            f.write(
                f"Execution Mode  : {mode.upper()}\n"
            )

            f.write(
                f"Execution Time  : {duration:.2f} sec\n"
            )

            f.write(
                "Executed On     : "
                f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            )

            f.write("\n")

            f.write("="*70+"\n")

            f.write("Reason\n")

            f.write("="*70+"\n\n")

            f.write(str(reason))

            f.write("\n")


    @classmethod
    def clear(cls, module):

        file = cls.LATEST / f"{module}.txt"

        if file.exists():

            file.unlink()