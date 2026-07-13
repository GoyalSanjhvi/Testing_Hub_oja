"""
execution_observer.py

Handles execution state transitions.
"""

from src.framework.observer.execution_status import ExecutionStatus

class ExecutionObserver:

    def waiting(self, result):

        result.status = ExecutionStatus.WAITING

        return result

    def running(self, result):

        result.status = ExecutionStatus.RUNNING

        return result

    def passed(self, result, duration):

        result.status = ExecutionStatus.PASS

        result.duration = duration

        return result

    def failed(self, result, duration):

        result.status = ExecutionStatus.FAIL

        result.duration = duration

        return result