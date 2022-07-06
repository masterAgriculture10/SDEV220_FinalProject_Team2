"""
File containing all the logic for the enroller app
"""

import enroller.ui as ui
from enroller.classes import Course


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
            start_time='11:00 AM', end_time='1:30 PM', days={'Tuesday', 'Friday'}),

        Course(name='SDEV 220', instructor='Feihong Liu', location='Gary', 
            start_time='5:00 PM', end_time='6:30 PM', days={'Monday', 'Wednesday'}),

        Course(name='ABCD 123', instructor='Sarah Evansborough', location='Evansborough', 
            start_time='7:30 PM', end_time='10:00 PM', days={'Tuesday', 'Thursday'}),
    ]

    while True:
        ui.display_courses(courses)
        selected = ui.select_course(courses)
        ui.display_new_enrollment(selected)

