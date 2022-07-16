"""
Terminal UI functionality and control loop for the terminal mockup
"""

from sys import exit
from typing import List, Optional, Tuple

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
    while True:
        display_courses(courses)
        selected = select_course(courses)
        display_new_enrollment(selected)
    

def find_user(users: List[Student], username: str, password: str) -> Optional[Student]:
    """Returns the user with the specified name and password if one exists"""
    for user in users:
        if user.username == username and user.password == password:
            return user


# display functions start here

def start_display() -> None:
    """Displays the initial state of the application"""
    print('--------------------')
    print('| Student Enroller |')
    print('--------------------')
    print('Log In (^C to exit)')


def prompt_login() -> Tuple[str, str]:
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
    print('Invalid username or password.')


def display_courses(courses: List[Course]) -> None:
    """Displays the input list of courses"""
    print('Courses:')
    for i in range(len(courses)):
        print(f'({i+1})', courses[i].name)
    print()


def select_course(courses: List[Course]) -> Course:
    """TODO: docstring"""

    while True:
        try:
            choice_input = input(f'Choose a course to enroll in (1-{len(courses)}, ^C to exit): ')
        except KeyboardInterrupt:
            print('^C\nexiting...')
            exit()
        
        try:
            course_num = int(choice_input)
            if not 1 <= course_num <= len(courses):
                raise ValueError
            return courses[course_num-1]
            
        except ValueError:
            print(f'Value must be between 1 and {len(courses)}.')


def display_new_enrollment(course: Course):
    print(f'You are now enrolled in {course.name}.')
    print()

