"""
Course Manager
07/25/2022
version 3.0
Authors:  Yahya G. Alrobaie, Gunnar Dahl, Alvin Hampton, Shanika N. Person

This program allows users to view and enroll in college courses.

GUI includes: 
- Login window that authenticates users
- Course tab that allows the user to view and select courses to enroll in
- Schedule tab that allows the user to view the courses they are enrolled in

The user's schedule is saved locally across sessions.
"""

from course_manager.gui import CourseApp

def main() -> None:
    """Runs the gui app"""
    CourseApp().mainloop()


if __name__ == '__main__':
    main()