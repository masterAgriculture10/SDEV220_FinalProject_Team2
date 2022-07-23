"""
These classes are used in the course manager application for the SDEV 220 final project.
"""

from dataclasses import dataclass, field
from enum import Enum
from datetime import time
from itertools import combinations
from typing import Dict, List, Optional, Set


class Day(Enum):
    """A day of the week\n
    (0 -> Sunday, 6 -> Saturday)"""
    (SUN, MON, TUE, WED, THU, FRI, SAT) = range(7)


class Course:
    "Contains information about the course instructor, location, and scheduling"

    _id_counter:int = 0

    def __init__(self, name:str, instructor:str, location:str, 
                 start_time:time, end_time:time, days:List[Day], 
                 *, id:Optional[int] = None) -> None:
        if id is None:
            self.id = Course._id_counter
            Course._id_counter += 1
        else:
            self.id = id
            Course._id_counter = max(Course._id_counter, id+1)

        self.name = name
        self.instructor = instructor
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.days = days

    def overlaps_with(self, other:'Course') -> bool:
        """whether another course's time and day overlap with this one's"""
        if len(set(self.days).intersection(set(other.days))) == 0:
            return False
        if self.end_time <= other.start_time:
            return False
        if other.end_time <= self.start_time:
            return False
        return True
    
    @classmethod
    def from_json(cls, json:Dict) -> 'Course':
        start_time = time.fromisoformat(json['start_time'])
        end_time = time.fromisoformat(json['end_time'])
        days = [Day[day_name] for day_name in json['days']]
        
        return cls(json['name'], json['instructor'], json['location'], 
                   start_time, end_time, days, id=json['id'])
    
    def to_json(self) -> Dict:
        start_str = time.isoformat(self.start_time, 'minutes')
        end_str = time.isoformat(self.end_time, 'minutes')
        day_str_list = [day.name for day in self.days]

        return {
            'id':           self.id,
            'name':         self.name,
            'instructor':   self.instructor,
            'location':     self.location,
            'start_time':   start_str,
            'end_time':     end_str,
            'days':         day_str_list,
        }  


@dataclass
class Student:
    """Contains the student's account information and the list of courses they are taking"""
    username: str
    password: str
    courses: List[Course] = field(default_factory=list)

    def has_overlaps(self) -> bool:
        """whether any courses in the list overlap each other"""
        combos = combinations(self.courses, 2)
        pair_overlaps = [a.overlaps_with(b) for a,b in combos]
        return (True in pair_overlaps)

    @classmethod
    def from_json(cls, json:Dict, all_courses:List[Course]) -> 'Student':
        student_courses = list(filter(lambda course: course.id in json['courses'], all_courses))
        return cls(json['username'], json['password'], student_courses)
    
    def to_json(self, all_courses: List[Course]) -> Dict:
        def find_course_by_name(course:Course, course_list:List[Course]):
            return next(filter(lambda c: c.name==course.name, course_list))
        id_list = list(map(lambda c:find_course_by_name(c, all_courses).id, self.courses))
        
        return {'username':self.username, 'password':self.password, 'courses':id_list}