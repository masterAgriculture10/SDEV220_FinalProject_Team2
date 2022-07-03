"""
Terminal Proof-of-Concept

This program is meant to contain the functionality of the GUI app we are building 
without worrying about the graphical part. It will allow us figure out the backend 
implementation before (or as) we make the front end.
"""

import ui


def main() -> None:
    ui.start_display()
    username = login()
    # select_courses()


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
    }
    
    try:
        return users[username] == password
    except KeyError:
        return False


if __name__ == '__main__':
    main()