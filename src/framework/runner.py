"""
runner.py

Executes automation modules.
"""

from importlib import import_module
from time import time

from src.framework.models.result import Result
from src.framework.observer.execution_observer import ExecutionObserver
from src.framework.output import Output
from src.framework.report import Report


class Runner:

    def __init__(

        self,

        page,

        mode,

        module_path

    ):

        self.page = page

        self.mode = mode

        self.observer = ExecutionObserver()

        self.module_path = module_path

        self.modules = import_module(

            module_path

        ).MODULES

    # --------------------------------------------------
    # Execute Module
    # --------------------------------------------------

    def run(

        self,

        module

    ):

        result = Result(

            module

        )

        self.observer.waiting(

            result

        )

        self.observer.running(

            result

        )

        start = time()

        try:

            status = self.modules[

                module

            ](

                self.page

            ).execute()

            duration = round(

                time() - start,

                2

            )

            if status:

                Output.clear(

                    module

                )

                self.observer.passed(

                    result,

                    duration

                )

                Report.update(

                    module=module,

                    status="PASS",

                    duration=duration

                )

            else:

                Output.save_error(

                    module=module,

                    mode=self.mode,

                    duration=duration,

                    reason="Verification Failed"

                )

                self.observer.failed(

                    result,

                    duration

                )

                Report.update(

                    module=module,

                    status="FAIL",

                    duration=duration

                )

        except Exception as e:

            duration = round(

                time() - start,

                2

            )

            Output.save_error(

                module=module,

                mode=self.mode,

                duration=duration,

                reason=e

            )

            self.observer.failed(

                result,

                duration

            )

            Report.update(

                module=module,

                status="FAIL",

                duration=duration

            )

        return result.to_dict()