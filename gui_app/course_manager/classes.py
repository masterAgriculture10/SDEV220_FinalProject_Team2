"""
These classes are used in the course manager application for the SDEV 220 final project.
"""

from dataclasses import dataclass, field
from enum import Enum
from datetime import time
from itertools import combinations
from typing import Dict, List, Optional


CREDIT_LIMIT = 15


class Day(Enum):
    """A day of the week\n
    (0 -> Sunday, 6 -> Saturday)"""
    (SUN, MON, TUE, WED, THU, FRI, SAT) = range(7)


class Course:
    "Contains information about the course instructor, location, and scheduling"

    _id_counter:int = 0

    def __init__(self, name:str, instructor:str, location:str, style:str,
                 start_time:time, end_time:time, days:List[Day], credit_hours:int, 
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
        self.style = style
        self.start_time = start_time
        self.end_time = end_time
        self.days = days
        self.credit_hours = credit_hours

    def __str__(self) -> str:
        def format_time(t:time) -> str:
            return t.strftime("%I:%M%p").lower().strip('0')
        
        s = f'{self.name} - {self.style} - {self.instructor} - {self.location} - '
        s += f'{format_time(self.start_time)}-{format_time(self.end_time)} - '
        for day in self.days:
            s += day.name.capitalize() + ','
        return s[:-1] + f' - {self.credit_hours} credit hours'

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

        try:
            id = json['id']
        except KeyError:
            id = None
        
        return cls(json['name'], json['instructor'], json['location'], json['style'],
                   start_time, end_time, days, json['credit_hours'], id=id)
    
    def to_json(self) -> Dict:
        start_str = time.isoformat(self.start_time, 'minutes')
        end_str = time.isoformat(self.end_time, 'minutes')
        day_str_list = [day.name for day in self.days]

        return {
            'id':           self.id,
            'name':         self.name,
            'instructor':   self.instructor,
            'location':     self.location,
            'style':        self.style,
            'start_time':   start_str,
            'end_time':     end_str,
            'days':         day_str_list,
            'credit_hours': self.credit_hours,
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
    
    def is_over_credit_limit(self) -> bool:
        return sum([c.credit_hours for c in self.courses]) > CREDIT_LIMIT

    @classmethod
    def from_json(cls, json:Dict, all_courses:List[Course]) -> 'Student':
        student_courses = [c for c in all_courses if c.id in json['courses']]
        return cls(json['username'], json['password'], student_courses)
    
    def to_json(self, all_courses: List[Course]) -> Dict:
        def find_course_by_name(search_name:str, course_list:List[Course]):
            return [c for c in course_list if c.name == search_name][0]
        id_list = [find_course_by_name(c.name, all_courses).id for c in self.courses]
        
        return {'username':self.username, 'password':self.password, 'courses':id_list}