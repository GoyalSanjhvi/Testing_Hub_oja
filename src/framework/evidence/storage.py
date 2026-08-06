"""
storage.py

Evidence storage.
"""

from pathlib import Path
import shutil


class EvidenceStorage:

    ROOT = Path("src/outputs/latest")

    @classmethod
    def application_folder(
        cls,
        application
    ):

        folder = cls.ROOT / application

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder

    @classmethod
    def module_folder(
        cls,
        application,
        module
    ):

        folder = (

            cls.application_folder(
                application
            )

            / module

        )

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder

    @classmethod
    def clear_module(
        cls,
        application,
        module
    ):

        folder = (

            cls.application_folder(
                application
            )

            / module

        )

        if folder.exists():

            shutil.rmtree(folder)

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder