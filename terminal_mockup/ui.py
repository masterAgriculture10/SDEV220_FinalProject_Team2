"""
Terminal UI functionality for the terminal mockup
"""

def start_display() -> None:
    """Displays the initial state of the application"""
    print('--------------------')
    print('| Student Enroller |')
    print('--------------------')
    print('Log In')


def prompt_login() -> tuple[str, str]:
    """Prompts the user to enter their username and password and returns them"""
    username = input('username: ')
    password = input('password: ')
    print()
    return username, password


def display_invalid_login() -> None:
    print('Invalid username or password.')


