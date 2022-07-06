"""
File containing all the logic for the enroller app
"""

import enroller.ui as ui


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


def select_courses() -> None:
    courses = [
        'SDEV 140',
        'SDEV 220',
        'ABCD 123',
    ] # TODO: this will be a list of objects later

    while True:
        ui.display_courses(courses)
        selected = ui.select_course(courses)
        ui.display_new_enrollment(selected)

