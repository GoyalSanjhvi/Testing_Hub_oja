from time import time

from src.framework.models.result import Result 

from src.framework.observer.execution_observer import ExecutionObserver 

from src.applications.oja.modules import MODULES


class Runner:

    def __init__(self, page):

        self.page = page

        self.observer = ExecutionObserver()

    def run(self, module):

        result = Result(module)

        self.observer.waiting(result)

        self.observer.running(result)

        start = time()

        try:

            status = MODULES[module](self.page).execute()

            duration = round(time() - start, 2)

            if status:

                self.observer.passed(result, duration)

            else:

                self.observer.failed(result, duration)

        except Exception as e:

            print(e)

            duration = round(time() - start, 2)

            self.observer.failed(result, duration)

        return result.to_dict()