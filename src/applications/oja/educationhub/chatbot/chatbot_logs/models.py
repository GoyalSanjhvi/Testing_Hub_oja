"""
models.py

Chatbot log model.
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ChatbotLog:

    module: str

    status: str

    execution_time: str

    duration: float

    questions: List[Dict] = field(default_factory=list)

    def to_dict(self):

        return {

            "module": self.module,

            "status": self.status,

            "execution_time": self.execution_time,

            "duration": self.duration,

            "questions": self.questions

        }