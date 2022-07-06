"""
Terminal Proof-of-Concept

This program is meant to contain the functionality of the GUI app we are building 
without worrying too much about the graphical part. It will allow us figure out the backend 
implementation before (or as) we make the front end.

This is the entry point for the program.
"""

import enroller.ui as ui
import enroller.logic as logic


def main() -> None:
    ui.start_display()
    username = logic.login()
    logic.select_courses(username)


if __name__ == '__main__':
    main()