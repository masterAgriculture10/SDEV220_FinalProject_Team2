"""
tkinter gui
"""

import tkinter as tk
from tkinter import Frame, ttk, font, ANCHOR

from .classes import Student
from .resources import load_json, save_json


# the current logged-in user
active_user:Student = None


def on_closing(frame, courses, students):
        """Saves and closes the app"""
        save_json(courses, students)
        frame.quit()



class CourseApp(tk.Tk):
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                courses, students = load_json()
                self.protocol("WM_DELETE_WINDOW", lambda c=courses,s=students:on_closing(self,c,s))

                # the container is where we'll stack a bunch of frames
                # on top of each other, then the one we want visible
                # will be raised above the others
                self.shared_data = {'StartPage':tk.StringVar()}
                container=tk.Frame(self)
                container.pack(side="top", fill="both", expand=True)
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                self.frames = {}
                i = 0
                for F in (StartPage, CoursesPage, Acct101Page, Bio101Page, Dbms110Page, Desn220Page, Engr195Page, Hvac170Page, Legs170Page, Math137Page, Sdev220Page):
                        page_name = F.__name__

                        if issubclass(F, CourseFrame):
                                # pass in courses with the same name as the class to put in listbox
                                filtered_courses = [c for c in courses if c.name == F.name]
                                frame = F(parent=container, controller=self, listbox_courses=filtered_courses, course_index=i)
                                i += 1
                        elif issubclass(F, StartPage):
                                frame = F(parent=container, controller=self, students=students, courses=courses)
                        else:
                                frame = F(parent=container, controller=self)

                        self.frames[page_name] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
                
                self.show_frame("StartPage")
        

        def show_frame(self, page_name):
                '''Show a frame for the given page name'''
                frame=self.frames[page_name]
                frame.tkraise()
                if isinstance(frame, CourseFrame):
                        frame.update_elements()



class StartPage(tk.Frame):
        """A frame that contains the elements of the login screen"""
        def __init__(self, parent, controller, students, courses):
                # the Frame that controls everything we add to the page
                tk.Frame.__init__(self, parent, bg='#003366')
                self.controller=controller
                
                self.controller.title('IVY Courses Registration')
                # options for the screen size: normal, iconic, withdrawn, or zoomed
                self.controller.state('normal')

                # notebook for just the login page
                login_notebook = ttk.Notebook(self, width=638, height=395)
                login_notebook.pack()
                
                login_tab = Frame(login_notebook, bg="#003366",)
                login_tab.pack()
                login_notebook.add(login_tab, text="Login")


                # header labels
                header_lbl = tk.Label(login_tab, text="IVY Courses Registration", fg='white', bg='#660066', font=('bold', 45))
                header_lbl.pack()

                selection_lbl = tk.Label(login_tab, text="Log In to Your Account:", fg='white', bg='#003366', font=('bold', 20), anchor='w')
                selection_lbl.place(x=0, y=60)


                # username label & entry box
                user_label = tk.Label(login_tab, text='Enter your username:', font=15, fg='white', bg='#003366')
                user_label.place(x=8, y=150)

                username = tk.StringVar()      
                username_entry_box = tk.Entry(login_tab, textvariable=username)
                username_entry_box.focus_set()
                username_entry_box.place(x=170, y=150)


                # password label & entry box
                password_label = tk.Label(login_tab, text='Enter your password:', font=15, fg='white', bg='#003366')
                password_label.place(x=8, y=190) 

                password = tk.StringVar()      
                password_entry_box = tk.Entry(login_tab, textvariable=password)
                password_entry_box.place(x=170, y=190)


                def find_user(username, password, users):
                        matching_users = [u for u in users if u.username==username and u.password==password]
                        return matching_users[0] if len(matching_users) != 0 else None
                
                
                def try_login():
                        """validates the input credentials"""
                        input_username = username.get()
                        input_password = password.get()

                        password.set('')

                        if input_username == input_password == '':
                                login_error_lbl['text']='Enter your username and password'

                        elif (found_user := find_user(input_username, input_password, students)) is not None:
                                username.set('')
                                login_error_lbl['text']=''
                                controller.show_frame('CoursesPage')
                                global active_user
                                active_user = found_user

                        else:
                                login_error_lbl['text']='Incorrect username or password'


                def clear_text():
                        """clears the text in the entry boxes"""
                        username_entry_box.delete(0, tk.END)
                        password_entry_box.delete(0, tk.END)
                

                # submit, exit, clear buttons
                submit_button = tk.Button(login_tab, text='Enter', command=try_login, relief='raised', width=10, height=2, borderwidth=3)
                submit_button.place(x=45, y=270)

                clear_button = tk.Button(login_tab, text="Clear", command=clear_text, relief='raised', width=10, height=2, borderwidth=3)
                clear_button.place(x=230, y=270)

                quit_button = tk.Button(login_tab, text="Exit", command=lambda c=courses,s=students:on_closing(self,c,s), 
                                        relief='raised', width=10, height=2, borderwidth=3)
                quit_button.place(x=420, y=270)


                # create a message label to display when the user enters an incorrect login 
                login_error_lbl = tk.Label(login_tab, text="", fg='white', bg='#003366', font=('bold', 22), anchor='n')
                login_error_lbl.place(x=180, y=220)



class CoursesPage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent, bg='#660066')
                self.controller=controller


                # create a notebook and its tab frames
                notebook = ttk.Notebook(self, width=638, height=395)
                notebook.pack()

                courses_tab = Frame(notebook, bg='#003366')
                courses_tab.pack()

                global schedule_tab
                schedule_tab = Frame(notebook, bg="#003366")
                schedule_tab.pack()

                notebook.add(courses_tab, text="Courses")
                notebook.add(schedule_tab, text="Schedule")
                

                # labels for the courses tab
                courses_header_lbl = tk.Label(courses_tab, text="IVY Courses", width=600, fg='white', bg='#660066', font=('bold', 30))
                courses_header_lbl.pack()

                selection_lbl= tk.Label(courses_tab, text="Select a course to enroll in", fg='white', bg='#003366', font=('bold', 20), anchor='w')
                selection_lbl.place(x=0, y=40)


                # make course buttons using a for loop
                # (class, x, y)
                button_values = (
                        (Acct101Page, 0,   100),
                        (Bio101Page,  210, 100),
                        (Dbms110Page, 420, 100),
                        (Desn220Page, 0,   178),
                        (Engr195Page, 210, 178),
                        (Hvac170Page, 420, 178),
                        (Legs170Page, 0,   256),
                        (Math137Page, 210, 256),
                        (Sdev220Page, 420, 256),
                )
                
                for (cls, x, y) in button_values:
                        button = tk.Button(courses_tab, text=cls.name, 
                                                command=lambda cls_name=cls.__name__:controller.show_frame(cls_name), 
                                                relief='raised', borderwidth=3, width=20, height=4)
                        button.place(x=x, y=y)


                # make a logout button  
                def log_out():
                        global active_user
                        active_user = None
                        controller.show_frame('StartPage')

                logout_button = tk.Button(courses_tab, text="Log Out", command=log_out, 
                                        relief='raised', borderwidth=2, width=10, height=2)
                logout_button.place(x=515, y=0)



class CourseFrame(tk.Frame):
        """Base class for creating course frames"""

        def __init__(self, parent, controller, course_name, course_list, course_index):
                tk.Frame.__init__(self, parent, bg='#660066')
                self.controller=controller

                # create a notebook just for this course
                this_course_notebook = ttk.Notebook(self, width=638, height=395)
                this_course_notebook.pack()
                
                this_course_tab = Frame(this_course_notebook, bg="#003366")
                this_course_tab.pack()

                this_course_notebook.add(this_course_tab, text=course_name)


                # header label
                header_lbl = tk.Label(this_course_tab, text="Select a course to enroll in: ", fg='white', bg='#003366', font=('bold', 20), anchor='w')
                header_lbl.place(x=0, y=0)


                # listbox
                bold_font = font.Font(weight='bold')
                course_listbox = tk.Listbox(this_course_tab, font=bold_font, relief='raised', borderwidth=4, width=70, height=4, selectmode=tk.BROWSE)
                course_listbox.place(x=0, y=30)
                
                for course in course_list:
                        course_listbox.insert(tk.END, str(course))


                # enroll & unenroll buttons
                def enroll():
                        selected_item = course_listbox.get(ANCHOR)

                        global active_user
                        for offered_course in course_list:
                                if str(offered_course) == selected_item:
                                        active_user.courses.append(offered_course)
                                        break

                        update_elements()

                def unenroll():
                        global active_user
                        for offered_course in course_list:
                                if offered_course in active_user.courses:
                                        active_user.courses.remove(offered_course)
                                        break

                        update_elements()

                def update_elements():
                        """Accurately displays active_user's selected course and [un]enroll buttons"""
                        global active_user
                        for offered_course in course_list:
                                if offered_course in active_user.courses:
                                        course_text = str(offered_course)
                                        enrolled_course_lbl.config(text=course_text)
                                        schedule_lbl.config(text=course_text)
                                        enroll_button['state'] = tk.DISABLED
                                        unenroll_button['state'] = tk.NORMAL
                                        break
                        else:
                                enrolled_course_lbl.config(text='')
                                schedule_lbl.config(text='')
                                enroll_button['state'] = tk.NORMAL
                                unenroll_button['state'] = tk.DISABLED
                
                # give access to update_elements from outside __init__
                self.update_elements = update_elements
                
                enroll_button = tk.Button(this_course_tab, text="Enroll", relief='raised', command=enroll, borderwidth=3, width=15, height=3)
                enroll_button.place(x=40, y=180)

                unenroll_button = tk.Button(this_course_tab, text="Unenroll", relief='raised', command=unenroll, borderwidth=3, width=15, height=3)
                unenroll_button.place(x=229, y=180)


                # display the enrolled class
                enrolled_course_lbl = tk.Label(this_course_tab, text='Enrolled class will appear here.', fg='white', bg='#333333', 
                                               borderwidth=5, relief='raised', width=65, height=2)
                enrolled_course_lbl.place(x=7, y=120)


                # display the enrolled class in the schedule
                schedule_lbl = tk.Label(schedule_tab, text='Enrolled class will appear here.', fg='white', bg='#333333', borderwidth=5, relief='raised', width=65, height=2)
                schedule_lbl.place(x=7, y=45*course_index+2)


                # back button
                back_button = tk.Button(this_course_tab, text="Back", relief='raised', borderwidth=3, width=15, height=3, 
                                        command=lambda:controller.show_frame('CoursesPage'))
                back_button.place(x=420, y=180)



# CourseFrame child classes

class Acct101Page(CourseFrame):
        name = "ACCT 101"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


class Bio101Page(CourseFrame):
        name = "BIO 101"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


class Dbms110Page(CourseFrame):
        name = "DBMS 110"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


class Desn220Page(CourseFrame):
        name = "DESN 220"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


class Engr195Page(CourseFrame):
        name = "ENGR 195"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


class Hvac170Page(CourseFrame):
        name = "HVAC 170"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


class Legs170Page(CourseFrame):
        name = "LEGS 170"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


class Math137Page(CourseFrame):
        name = "MATH 137"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


class Sdev220Page(CourseFrame):
        name = "SDEV 220"

        def __init__(self, parent, controller, listbox_courses, course_index):
                super().__init__(parent, controller, course_name=self.name, 
                                 course_list=listbox_courses, course_index=course_index)


