"""
Terminal Proof-of-Concept

This program is meant to contain the functionality of the GUI app we are building 
without worrying about the graphical part. It will allow us figure out the backend 
implementation before (or as) we make the front end.
"""


def main() -> None:
    username = login()
    # select_courses()


def login() -> str:
    """Returns the username of a user when they input valid credentials"""
    username, password = prompt_login()

    while not authenticate(username, password):
        username, password = prompt_login(again=True)

    return username


def prompt_login(again:bool=False) -> tuple[str, str]:
    """Prompts the user to enter their username and password and returns them"""
    if again:
        print('Invalid username or password.', end='\n\n')
    username = input('username: ')
    password = input('password: ')
    return username, password


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