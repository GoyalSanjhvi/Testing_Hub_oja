"""
logger.py

Console logger.
"""

from datetime import datetime


class Logger:

    @staticmethod
    def info(message):

        print(f"[INFO] {message}")

    @staticmethod
    def pass_log(module):

        print(

            f"[{datetime.now().strftime('%H:%M:%S')}] "

            f"PASS : {module}"

        )

    @staticmethod
    def fail(module):

        print(

            f"[{datetime.now().strftime('%H:%M:%S')}] "

            f"FAIL : {module}"

        )