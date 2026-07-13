"""
report.py

Stores execution results.
"""


class Report:

    def __init__(self):

        self.results = []

    def add(self, module, status, duration):

        self.results.append({

            "module": module,

            "status": status,

            "duration": duration

        })

    def all(self):

        return self.results