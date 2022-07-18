"""
File containing all the logic for the enroller app
"""

import json
from typing import List, Tuple

from enroller.classes import Course, Student


def load_json(filename:str) -> Tuple[List[Course], List[Student]]:
    with open(filename, 'rt') as file_in:
        stored_text = file_in.read()
    stored_json = json.loads(stored_text)
    courses = [Course.from_json(c) for c in stored_json['courses']]
    students = [Student.from_json(s, courses) for s in stored_json['students']]
    return courses, students


# Student('skywalker1', 'your_father'),
# Student('artwodeetwo', 'ceethreepeeoh'),
# Student('palpatino', 'THE_$ENATE'),
# Student('yahya', '0000'),


# Course(name='SDEV 140', instructor='John Bean', location='Nepal', 
#     start_time=time(11, 00), end_time=time(13, 30), days={Day.TUE, Day.FRI}),

# Course(name='SDEV 220', instructor='Feihong Liu', location='Gary', 
#     start_time=time(16, 00), end_time=time(18, 30), days={Day.MON, Day.WED}),

# Course(name='ABCD 123', instructor='Sarah Evanston', location='Sacramento', 
#     start_time=time(19, 30), end_time=time(22, 00), days={Day.TUE, Day.THU}),

