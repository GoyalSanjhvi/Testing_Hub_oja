"""
config.py

Loads application configuration.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    BASE_URL = os.getenv("BASE_URL")

    EMAIL = os.getenv("EMAIL")

    PASSWORD = os.getenv("PASSWORD")