"""
Terminal UI functionality and control loop for the terminal mockup
"""

from sys import exit
from typing import List, NoReturn, Optional, Tuple, Union

from .classes import Course, Schedule, Student
from .resources import load_json, save_json


def do_terminal_program(): 
    """Does login and course select"""

    courses, students = load_json()

    # login
    start_display()
    username, password = prompt_login()
    user = find_user(students, username, password)
    while user is None:
        display_invalid_login()
        username, password = prompt_login()
        user = find_user(students, username, password)

    # course select
    display_welcome()
    while True:
        interpret_command(prompt_command(), user, courses, students)
    

def find_user(users: List[Student], username: str, password: str) -> Optional[Student]:
    """Returns the user with the specified name and password if one exists"""
    for user in users:
        if user.username == username and user.password == password:
            return user


def interpret_command(command_text: str, student: Student, course_list: List[Course], 
                      student_list:List[Student]) -> Union[None, NoReturn]:
    """Takes a command string, parses it, and performs it"""
    if command_text.strip() == '': 
        return
    
    command, *args = command_text.strip().lower().split(maxsplit=1)
    arg = args[0] if args != [] else None
    
    if command == 'courses':
        display_courses(course_list)

    elif command == 'enroll':
        enroll_in(arg, student.schedule, course_list)

    elif command == 'unenroll':
        unenroll_in(arg, student.schedule)

    elif command == 'schedule':
        print(f"{student.username}'s schedule:")
        display_courses(student.schedule.courses)

    elif command == 'save':
        save_json(course_list, student_list)
        print("your schedule has been saved")

    elif command == 'help':
        print("commands: 'courses', '[un]enroll <course name>', 'schedule', 'save', 'help', 'exit'")

    elif command == 'exit':
        print('exiting...')
        exit()

    else:
        print("invalid command, enter 'help' for a list of commands")
    
    print()


def enroll_in(course_name:Optional[str], schedule:Schedule, course_list:List[Course]) -> None:

    if course_name is None:
        print("please provide the name of the course")
        return

    selected_courses = list(filter(lambda course: course.name.lower() == course_name, course_list))
    if len(selected_courses) == 0:
        print(f"no course with name {course_name}")
        return
    
    in_schedule = len(list(filter(lambda course: course.name.lower() == course_name, schedule.courses))) > 0
    if in_schedule:
        print("this course is already in your schedule")
        return
    
    schedule.courses.append(selected_courses[0])
    print(f"added {course_name} to your schedule")


def unenroll_in(course_name:Optional[str], schedule:Schedule) -> None:

    if course_name is None:
        print("please provide the name of the course")
        return
    
    new_course_list = list(filter(lambda course: course.name.lower() != course_name, schedule.courses))
    if len(new_course_list) == len(schedule.courses):
        print("this course is not in your schedule")
        return
    
    schedule.courses = new_course_list
    print(f"removed {course_name} from your schedule")


# display functions start here

def start_display() -> None:
    """Displays the initial state of the application"""
    print('------------------')
    print('| COURSE MANAGER |')
    print('------------------')
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

