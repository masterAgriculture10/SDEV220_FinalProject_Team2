"""
Terminal UI functionality for the terminal mockup
"""

from sys import exit
from typing import List, Tuple

from enroller.classes import Course


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
    print(f'You are now enrolled in {course.name}.',)
    print()

