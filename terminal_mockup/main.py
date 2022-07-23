"""
Terminal Proof-of-Concept

This program is meant to contain the functionality of the GUI app we are building 
without worrying too much about the graphical part. It will allow us figure out the backend 
implementation before (or as) we make the front end.

This is the entry point for the program.

Commands: 
courses
[un]enroll <course name>
schedule
save
help
exit
"""

from typing import NoReturn

from enroller.terminal_io import do_terminal_program


def main() -> NoReturn:
    """Starts the terminal app"""
    do_terminal_program()


if __name__ == '__main__':
    main()