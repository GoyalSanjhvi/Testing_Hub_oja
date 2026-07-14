"""
execution_service.py

Handles module execution.
"""

from src.framework.browser import Browser
from src.framework.runner import Runner
from src.framework.output import Output
from src.framework.report import Report


class ExecutionService:

    @staticmethod
    def run(module, mode):

        if module == "Login":

            Output.start_execution()

            Report.initialize(mode)

        browser = Browser(mode)

        try:

            page = browser.open()

            runner = Runner(

                page,

                mode

            )

            return runner.run(module)

        except Exception as e:

            print(e)

            return {

                "module": module,

                "status": "FAIL",

                "duration": 0

            }

        finally:

            browser.close()