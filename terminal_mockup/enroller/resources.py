"""
File containing all the logic for the enroller app
"""

from datetime import time
from typing import Dict, List

from enroller.classes import Course, Day


def get_users() -> Dict[str, str]:
    return {
        'skywalker1': 'your_father',
        'artwodeetwo': 'ceethreepeeoh',
        'palpatino': 'THE_$ENATE',
        'yahya': '0000',
    }


def get_courses() -> List[Course]:
    return [
        Course(name='SDEV 140', instructor='John Bean', location='Nepal', 
            start_time=time(11, 00), end_time=time(13, 30), days={Day.TUE, Day.FRI}),

        Course(name='SDEV 220', instructor='Feihong Liu', location='Gary', 
            start_time=time(16, 00), end_time=time(18, 30), days={Day.MON, Day.WED}),

        Course(name='ABCD 123', instructor='Sarah Evansborough', location='Sacramento', 
            start_time=time(19, 30), end_time=time(22, 00), days={Day.TUE, Day.THU}),
    ]

