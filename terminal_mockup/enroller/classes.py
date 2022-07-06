"""
These classes are used in the enroller application for the SDEV 220 final project.
"""

from dataclasses import dataclass


@dataclass
class Course:
    name: str
    instructor: str
    location: str
    start_time: str
    end_time: str
    days: "list[str]"

