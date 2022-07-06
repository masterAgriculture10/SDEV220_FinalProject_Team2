"""
These classes are used in the enroller application for the SDEV 220 final project.
"""

from dataclasses import dataclass
from enum import Enum
from datetime import time


class Day(Enum):
    """A day of the week"""
    (SUN, MON, TUE, WED, THU, FRI, SAT) = range(7)


@dataclass
class Course:
    name: str
    instructor: str
    location: str
    start_time: time
    end_time: time
    days: "set[Day]"


