"""
reader.py

Reads execution logs and evidence.
"""

import json

from .storage import EvidenceStorage


class EvidenceReader:

    @classmethod
    def execution_log(

        cls,

        application,

        module

    ):
        """
        Return execution log.
        """

        file = (

            EvidenceStorage.module_folder(

                application,

                module

            )

            / "execution.log"

        )

        if not file.exists():

            return ""

        return file.read_text(

            encoding="utf-8"

        )

    @classmethod
    def steps(

        cls,

        application,

        module

    ):
        """
        Return all evidence steps.
        """

        file = (

            EvidenceStorage.module_folder(

                application,

                module

            )

            / "steps.json"

        )

        if not file.exists():

            return []

        with open(

            file,

            encoding="utf-8"

        ) as fp:

            return json.load(fp)

    @classmethod
    def total_steps(

        cls,

        application,

        module

    ):
        """
        Total evidence steps.
        """

        return len(

            cls.steps(

                application,

                module

            )

        )

    @classmethod
    def screenshots(

        cls,

        application,

        module

    ):
        """
        Return screenshots only.
        """

        return [

            step["screenshot"]

            for step in cls.steps(

                application,

                module

            )

        ]

    @classmethod
    def html_files(

        cls,

        application,

        module

    ):
        """
        Return html files only.
        """

        return [

            step["html"]

            for step in cls.steps(

                application,

                module

            )

        ]