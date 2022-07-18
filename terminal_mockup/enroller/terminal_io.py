"""
Terminal UI functionality and control loop for the terminal mockup
"""

from sys import exit
from typing import List, NoReturn, Optional, Tuple, Union

from enroller.classes import Course, Schedule, Student
import enroller.resources as resources


def do_terminal_program(): 
    """Does login and course select"""
    # login
    start_display()
    users = resources.get_users()

    username, password = prompt_login()
    user = find_user(users, username, password)
    while user is None:
        display_invalid_login()
        username, password = prompt_login()
        user = find_user(users, username, password)

    # course select
    courses = resources.get_courses()
    display_welcome()
    while True:
        interpret_command(prompt_command(), user, courses)
    

def find_user(users: List[Student], username: str, password: str) -> Optional[Student]:
    """Returns the user with the specified name and password if one exists"""
    for user in users:
        if user.username == username and user.password == password:
            return user


def interpret_command(command_text: str, student: Student, course_list: List[Course]) -> Union[None, NoReturn]:
    """Takes a command string, parses it, and performs it"""
    if command_text.strip() == '': 
        return
    
    command, *arg = command_text.strip().lower().split(maxsplit=1)
    
    if command == 'courses':
        display_courses(course_list)
    elif command == 'enroll':
        raise NotImplementedError
    elif command == 'unenroll':
        raise NotImplementedError
    elif command == 'schedule':
        raise NotImplementedError
    elif command == 'save':
        raise NotImplementedError
    elif command == 'help':
        print("commands: 'courses', '[un]enroll <course name>', 'schedule', 'help', 'exit'")
    elif command == 'exit':
        print('exiting...')
        exit()
    else:
        print("invalid command, enter 'help' for a list of commands")
    
    print()


# display functions start here

def start_display() -> None:
    """Displays the initial state of the application"""
    print('--------------------')
    print('| STUDENT ENROLLER |')
    print('--------------------')
    print('log in')


def prompt_login() -> Union[Tuple[str, str], NoReturn]:
    """Prompts the user to enter their username and password and returns them"""
    try:
        username = input('username: ')
        password = input('password: ')
    except KeyboardInterrupt:
        print('^C\nexiting...')
        exit()
    
    print()
    return username, password


def display_invalid_login() -> None:
    print('invalid username or password')


def display_welcome() -> None:
    print("'exit' to end the program, 'help' for more information")


def prompt_command() -> Union[str, NoReturn]:
    """Prompts the user for a command and returns it"""
    try:
        return input('> ')
    except KeyboardInterrupt:
        print('^C\nexiting...')
        exit()


def display_courses(courses: List[Course]) -> None:
    """Displays the input list of courses
    TODO: display days correctly"""
    print(f'_{"Name":_<15}_|_{"Instructor":_<15}_|_{"Location":_<15}_|_'
          f'{"Starts":_<8}_|_{"Ends":_<8}_|_{"Days":_<15}')
    for c in courses:
        print(f' {c.name:<15} | {c.instructor:<15} | {c.location:<15} | '
              f'{c.start_time.isoformat(timespec="minutes"):>5}    | {c.end_time.isoformat(timespec="minutes"):>5}    | {"-unavailable-":<15}')

