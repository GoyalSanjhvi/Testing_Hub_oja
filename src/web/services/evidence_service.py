"""
evidence_service.py

Reads execution logs and evidence.
"""

from src.framework.evidence.storage import EvidenceStorage

import json


class EvidenceService:

    @staticmethod
    def logs(

        application,

        module

    ):

        file = (

            EvidenceStorage.module_folder(

                application,

                module

            )

            / "execution.log"

        )

        if not file.exists():

            return {

                "logs": ""

            }

        return {

            "logs": file.read_text(

                encoding="utf-8"

            )

        }

    @staticmethod
    def evidence(

        application,

        module

    ):

        file = (

            EvidenceStorage.module_folder(

                application,

                module

            )

            / "steps.json"

        )

        if not file.exists():

            return {

                "steps": []

            }

        with open(

            file,

            encoding="utf-8"

        ) as fp:

            return {

                "steps": json.load(

                    fp

                )

            }