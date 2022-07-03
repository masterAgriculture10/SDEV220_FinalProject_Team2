"""
Terminal UI functionality for the terminal mockup
"""

from sys import exit


def start_display() -> None:
    """Displays the initial state of the application"""
    print('--------------------')
    print('| Student Enroller |')
    print('--------------------')
    print('Log In (^C to exit)')


def prompt_login() -> tuple[str, str]:
    """Prompts the user to enter their username and password and returns them"""
    try:
        username = input('username: ')
        password = input('password: ')
    except KeyboardInterrupt:
        print('\nexiting...')
        exit()
    
    print()
    return username, password


def display_invalid_login() -> None:
    print('Invalid username or password.')


def display_courses(courses: list[str]) -> None:
    """Displays the input list of courses"""
    print('Courses:')
    for i in range(len(courses)):
        print(f'({i+1})', courses[i])
    print()


def select_course(courses: list[str]) -> str:
    """TODO: docstring"""
    try:
        choice_input = input(f'Choose a course to enroll in (1-{len(courses)}, ^C to exit): ')
    except KeyboardInterrupt:
        print('\nexiting...')
        exit()
    
    try:
        course_num = int(choice_input)
        if not 1 <= course_num <= len(courses):
            raise ValueError
        return courses[course_num-1]
        
    except ValueError:
        print('ValueError')


def display_new_enrollment(course: str):
    print(f'You are now enrolled in {course}.',)
    print()


