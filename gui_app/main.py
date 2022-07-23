"""
Course Manager GUI App

This program allows users to view and enroll in college courses.

GUI includes: 
- Login window that authenticates users
- Course tab that allows the user to view and select courses to enroll in
- Schedule tab that allows the user to view the courses they are enrolled in
"""

from course_manager.gui import CourseApp


def main() -> None:
    """Runs the gui app"""
    CourseApp().mainloop()


if __name__ == '__main__':
    main()