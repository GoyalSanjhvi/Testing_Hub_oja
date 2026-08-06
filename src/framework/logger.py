"""
logger.py

Framework logger.
"""

from datetime import datetime


class Logger:

    # --------------------------------------------------
    # Timestamp
    # --------------------------------------------------

    @staticmethod
    def time():

        return datetime.now().strftime(

            "%H:%M:%S"

        )

    # --------------------------------------------------
    # Info
    # --------------------------------------------------

    @classmethod
    def info(

        cls,

        message

    ):

        print(

            f"[{cls.time()}] "

            f"INFO : {message}"

        )

    # --------------------------------------------------
    # Success
    # --------------------------------------------------

    @classmethod
    def success(

        cls,

        message

    ):

        print(

            f"[{cls.time()}] "

            f"PASS : {message}"

        )

    # --------------------------------------------------
    # Failure
    # --------------------------------------------------

    @classmethod
    def fail(

        cls,

        message

    ):

        print(

            f"[{cls.time()}] "

            f"FAIL : {message}"

        )

    # --------------------------------------------------
    # Warning
    # --------------------------------------------------

    @classmethod
    def warning(

        cls,

        message

    ):

        print(

            f"[{cls.time()}] "

            f"WARN : {message}"

        )

    # --------------------------------------------------
    # Step
    # --------------------------------------------------

    @classmethod
    def step(

        cls,

        module,

        number,

        title

    ):

        print()

        print("=" * 70)

        print(

            f"[{cls.time()}] "

            f"{module} | STEP {number}"

        )

        print(title)

        print("=" * 70)

    # --------------------------------------------------
    # Screenshot
    # --------------------------------------------------

    @classmethod
    def screenshot(

        cls,

        path

    ):

        print(

            f"[{cls.time()}] "

            f"📸 {path}"

        )

    # --------------------------------------------------
    # HTML
    # --------------------------------------------------

    @classmethod
    def html(

        cls,

        path

    ):

        print(

            f"[{cls.time()}] "

            f"🌐 {path}"

        )

    # --------------------------------------------------
    # Module
    # --------------------------------------------------

    @classmethod
    def module(

        cls,

        module

    ):

        print()

        print("=" * 80)

        print(

            f"{module.upper()}"

        )

        print("=" * 80)