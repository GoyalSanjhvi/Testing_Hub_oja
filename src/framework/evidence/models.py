"""
models.py

Evidence models.
"""

from dataclasses import dataclass


@dataclass
class EvidenceStep:

    application: str

    module: str

    step: int

    title: str

    status: str

    timestamp: str

    screenshot: str

    html: str