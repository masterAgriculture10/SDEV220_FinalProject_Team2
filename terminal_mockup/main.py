"""
Terminal Proof-of-Concept

This program is meant to contain the functionality of the GUI app we are building 
without worrying too much about the graphical part. It will allow us figure out the backend 
implementation before (or as) we make the front end.

This is the entry point for the program.
"""

import enroller.terminal_io as io
import enroller.resources as resources


def main() -> None:
    """Runs the terminal app"""

    # login
    io.start_display()
    users = resources.get_users()
    username, password = io.prompt_login()

    while not authenticate(users, username, password):
        io.display_invalid_login()
        username, password = io.prompt_login()

    # course select
    courses = resources.get_courses()
    while True:
        io.display_courses(courses)
        selected = io.select_course(courses)
        io.display_new_enrollment(selected)


def authenticate(users: 'dict[str, str]', username: str, password: str) -> bool:
    """Determines whether the username-password pair appear in the users dictionary together"""
    try:
        return users[username] == password
    except KeyError:
        return False


if __name__ == '__main__':
    main()