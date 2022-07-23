"""
Functions for loading and saving persistent data
"""

import json
from os.path import join
from typing import List, Tuple

from .classes import Course, Student


def load_json() -> Tuple[List[Course], List[Student]]:
    path = join(__file__, '..', '..', 'saved_data.json')
    with open(path, 'rt') as file_in:
        stored_text = file_in.read()
    
    stored_json = json.loads(stored_text)
    courses = [Course.from_json(c) for c in stored_json['courses']]
    students = [Student.from_json(s, courses) for s in stored_json['students']]
    return courses, students


def save_json(courses:List[Course], students:List[Student]) -> None:
    json_courses = [c.to_json() for c in courses]
    json_students = [s.to_json(courses) for s in students]
    new_json = {'students': json_students, 'courses': json_courses}
    new_text = json.dumps(new_json, indent=4)

    path = join(__file__, '..', '..', 'saved_data.json')
    with open(path, 'wt') as file_out:
        file_out.write(new_text)