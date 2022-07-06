"""
File containing all the logic for the enroller app
"""

from datetime import time

import enroller.ui as ui
from enroller.classes import Course, Day


def login() -> str:
    """Returns the username of a user when they input valid credentials"""
    username, password = ui.prompt_login()

    while not authenticate(username, password):
        ui.display_invalid_login()
        username, password = ui.prompt_login()

    return username


def authenticate(username: str, password: str) -> bool:
    users = {
        'skywalker1': 'your_father',
        'artwodeetwo': 'ceethreepeeoh',
        'palpatino': 'THE_$ENATE',
        'yahya': '0000',
    }
    
    try:
        return users[username] == password
    except KeyError:
        return False


def select_courses(username: str) -> None:
    courses = [
        Course(name='SDEV 140', instructor='John Bean', location='Nepal', 
            start_time=time(11, 00), end_time=time(13, 30), days={Day.TUE, Day.FRI}),

        Course(name='SDEV 220', instructor='Feihong Liu', location='Gary', 
            start_time=time(16, 00), end_time=time(18, 30), days={Day.MON, Day.WED}),

        Course(name='ABCD 123', instructor='Sarah Evansborough', location='Evansborough', 
            start_time=time(19, 30), end_time=time(22, 00), days={Day.TUE, Day.THU}),
    ]

    while True:
        ui.display_courses(courses)
        selected = ui.select_course(courses)
        ui.display_new_enrollment(selected)

