"""
config.py

Loads application configuration.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    # --------------------------------------------------
    # Application
    # --------------------------------------------------

    BASE_URL = os.getenv("BASE_URL")

    # --------------------------------------------------
    # Browser
    # --------------------------------------------------

    HEADLESS = False

    LOAD_TIMEOUT = 15000

    WAIT_TIME = 2000

    # --------------------------------------------------
    # Accounts
    # --------------------------------------------------

    ACCOUNTS = {

        "patient": {

            "email": os.getenv("PATIENT_EMAIL"),

            "password": os.getenv("PATIENT_PASSWORD")

        },

        "doctor": {

            "email": os.getenv("DOCTOR_EMAIL"),

            "password": os.getenv("DOCTOR_PASSWORD")

        }

    }

    # --------------------------------------------------
    # Helper
    # --------------------------------------------------

    @classmethod
    def get_account(cls, account="patient"):

        if account not in cls.ACCOUNTS:

            raise ValueError(
                f"Unknown account: {account}"
            )

        return cls.ACCOUNTS[account]