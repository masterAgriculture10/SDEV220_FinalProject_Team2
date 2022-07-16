"""
These classes are used in the enroller application for the SDEV 220 final project.
"""

from dataclasses import dataclass
from enum import Enum
from datetime import time
import itertools
from typing import Optional, Set, Union
from typing_extensions import Self


class Day(Enum):
    """A day of the week"""
    (SUN, MON, TUE, WED, THU, FRI, SAT) = range(7)


@dataclass
class Course:
    "Contains information about the course instructor, location, and scheduling"
    name: str
    instructor: str
    location: str
    start_time: time
    end_time: time
    days: Set[Union[Day, int]]

    def overlaps_with(self, other:Self) -> bool:
        """whether another course's time and day overlap with this one's"""
        if len(self.days.intersection(other.days)) == 0:
            return False
        if self.end_time <= other.start_time:
            return False
        if other.end_time <= self.start_time:
            return False
        return True


class Schedule:
    """Contains a list of Courses that a student has selected"""
    def __init__(self, courses:Optional[Set[Course]]=None) -> None:
        if courses is None:
            courses = set()
        else: 
            self.courses = courses

    def has_overlaps(self) -> bool:
        """whether any courses in the list overlap each other"""
        combos = itertools.combinations(self.courses, 2)
        pair_overlaps = [a.overlaps_with(b) for a,b in combos]
        return (True in pair_overlaps)


@dataclass
class Student:
    """Contains the student's account information as well as the schedule they have made"""
    username: str
    password: str
    schedule: Schedule


