"""
execution_service.py

Handles module execution.
"""

from src.framework.browser import Browser
from src.framework.runner import Runner
from src.framework.output import Output
from src.framework.report import Report


class ExecutionService:

    APPLICATIONS = {

        "oja": "src.applications.oja.modules",

        "ojadoctor": "src.applications.ojadoctor.modules"

    }

    @classmethod
    def run(

        cls,

        application,

        module,

        mode

    ):

        if module == "Login":

            Output.start_execution()

            Report.initialize(

                mode

            )

        browser = Browser(

            mode

        )

        try:

            page = browser.open()

            module_path = cls.APPLICATIONS.get(

                application

            )

            if module_path is None:

                raise Exception(

                    f"Unknown application: {application}"

                )

            runner = Runner(

                page=page,

                mode=mode,

                module_path=module_path

            )

            return runner.run(

                module

            )

        except Exception as e:

            print(e)

            return {

                "module": module,

                "status": "FAIL",

                "duration": 0

            }

        finally:

            browser.close()