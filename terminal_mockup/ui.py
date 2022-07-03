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


