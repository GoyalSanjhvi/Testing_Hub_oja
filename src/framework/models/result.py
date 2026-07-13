"""
result.py
"""


class Result:

    def __init__(self, module):

        self.module = module

        self.status = "WAITING"

        self.duration = 0

    def to_dict(self):

        return {

            "module": self.module,

            "status": self.status,

            "duration": self.duration

        }