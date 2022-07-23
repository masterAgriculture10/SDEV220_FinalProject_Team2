"""
Course Manager
07/24/2022
version 3.0
Authors:  Yahya G. Alrobaie, Gunnar Dahl, Alvin Hampton, Shanika N. Person

This program allows users to view and enroll in college courses.

GUI includes: 
- Login window that authenticates users
- Course tab that allows the user to view and select courses to enroll in
- Schedule tab that allows the user to view the courses they are enrolled in
"""

import tkinter as tk
from tkinter import Frame, ttk, font, ANCHOR


database = {"yahya": "1111", "gunnar": "2222", "alvin": "3333", "shanika": "4444"}
print(f'account details: {database}')


class CourseApp(tk.Tk):
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

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
                for F in (StartPage, CoursesPage, Acct101Page, Bio101Page, Dbms110Page, Desn220Page, Engr195Page, Hvac171Page, Legs170Page, Math137Page, Sdev220Page):
                        page_name = F.__name__
                        frame = F(parent=container, controller=self)
                        self.frames[page_name] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
                
                self.show_frame("StartPage")
        

        def show_frame(self, page_name):
                '''Show a frame for the given page name'''
                frame=self.frames[page_name]
                frame.tkraise()


class StartPage(tk.Frame):
        """A frame that contains the elements of the login screen"""
        def __init__(self, parent, controller):
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


                def login_check():
                        """validates the input credentials"""
                        if username.get() in database :
                                if database[username.get()] == password.get() :
                                        password.set('')  
                                        username.set('')
                                        incorrect_login_label['text']=''
                                        controller.show_frame('CoursesPage')
                                else:
                                        incorrect_login_label['text']='Incorrect username or password'
                        elif password.get() == '' and username.get() == '':
                                incorrect_login_label['text']='Enter your username and password'
                        else:
                                incorrect_login_label['text']='Incorrect username or password'


                def clear_text():
                        """clears the text in the entry boxes"""
                        username_entry_box.delete(0, tk.END)
                        password_entry_box.delete(0, tk.END)
                

                # submit, exit, clear buttons
                submit_button = tk.Button(login_tab, text='Enter', command=login_check, relief='raised', width=10, height=2, borderwidth=3)
                submit_button.place(x=45, y=270)

                clear_button = tk.Button(login_tab, text="Clear", command=clear_text, relief='raised', width=10, height=2, borderwidth=3)
                clear_button.place(x=230, y=270)

                quit_button = tk.Button(login_tab, text="Exit", command=self.quit, relief='raised', width=10, height=2, borderwidth=3)
                quit_button.place(x=420, y=270)


                # create a message label to display when the user enters an incorrect login 
                incorrect_login_label = tk.Label(login_tab, text="", fg='white', bg='#003366', font=('bold', 22), anchor='n')
                incorrect_login_label.place(x=180, y=220)




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
                # (button text, class name, x, y)
                button_values = (
                        ('ACCT 101', 'Acct101Page', 0,   100),
                        ('BIO 101',  'Bio101Page',  210, 100),
                        ('DBMS 110', 'Dbms110Page', 420, 100),
                        ('DESN 220', 'Desn220Page', 0,   178),
                        ('ENGR 195', 'Engr195Page', 210, 178),
                        ('HVAC 171', 'Hvac171Page', 420, 178),
                        ('LEGS 170', 'Legs170Page', 0,   256),
                        ('MATH 137', 'Math137Page', 210, 256),
                        ('SDEV 220', 'Sdev220Page', 420, 256),
                )
                
                for (button_text, cls_name, x, y) in button_values:
                        button = tk.Button(courses_tab, text=button_text, 
                                                command=lambda cls_name=cls_name:controller.show_frame(cls_name), 
                                                relief='raised', borderwidth=3, width=20, height=4)
                        button.place(x=x, y=y)


                # make an logout button                
                exit_button = tk.Button(courses_tab, text="Log Out", 
                                        command=lambda:controller.show_frame('StartPage'), 
                                        relief='raised', borderwidth=2, width=10, height=2)
                exit_button.place(x=515, y=0)



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
                        course_listbox.insert(tk.END, course)


                # enroll & unenroll buttons
                def enroll():
                        enrolled_course_lbl.config(text=course_listbox.get(ANCHOR))
                        schedule_lbl.config(text=course_listbox.get(ANCHOR))
                        enroll_button['state'] = tk.DISABLED
                        unenroll_button['state'] = tk.NORMAL

                def unenroll():
                        enrolled_course_lbl.config(text='')
                        schedule_lbl.config(text='')
                        enroll_button['state'] = tk.NORMAL
                        unenroll_button['state'] = tk.DISABLED
                
                enroll_button = tk.Button(this_course_tab, text="Enroll", relief='raised', command=enroll, borderwidth=3, width=15, height=3)
                enroll_button.place(x=40, y=180)

                unenroll_button = tk.Button(this_course_tab, text="Unenroll", relief='raised', command=unenroll, borderwidth=3, width=15, height=3)
                unenroll_button.place(x=229, y=180)
                unenroll_button['state'] = tk.DISABLED


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
        def __init__(self, parent, controller):
                course_list = ["ACCT101 - Virtual - Sean Carter - M,W 10:00am-12:00pm - FortWayne - 8Wks - 3credits",
                               "ACCT101 - Learn Anywhere - Kim Kardashian - T,R 1:00pm-3:00pm - Columbus - 16Wks - 3credits",
                               "ACCT101 - Traditional - Curtis Jackson - F 3:00pm-6:00pm - N Meridian - 8Wks - 3credits"]

                CourseFrame.__init__(self, parent, controller, course_name="ACCT 101", course_list=course_list, course_index=0)


class Bio101Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["BIO101 - Traditional - Nye Bill - M,W 1:00pm-4:30pm - FortWayne - 8Wks - 3credits",
                          "BIO101 - Virtual - Professor X - T,R 6:00pm-9:30pm - Columbus - 16Wks - 3credits",
                          "BIO101 - Traditional - Bill Nye - T 1:00pm-5:00pm - N Meridian - 8Wks - 3credits"]

                CourseFrame.__init__(self, parent, controller, course_name="BIO 101", course_list=course_list, course_index=1)


class Dbms110Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["DBMS110 - Traditional - Anthony Stark - F 2:00pm-5:50pm - New York City - 16Wks - 3credits",
                          "DBMS110 - Virtual -  Stark Anthony - T,R 2:00pm-3:50pm - New York City - 8Wks - 3credits",
                          "DBMS110 - Traditional - Bruce Wayne - S 9:00am-12:50pm - Gotham - 16Wks - 3credits"]

                CourseFrame.__init__(self, parent, controller, course_name="DBMS 110", course_list=course_list, course_index=2)


class Desn220Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["DESN220 - Anywhere - Mark Zuckerberg - F 1:00pm-4:30pm - Plainfield - 16Wks - 3credits",
                           "DESN220 - Traditional - Steve Jobs Jr. - T,R 6:00pm-7:30pm - Indianapolis - 8Wks - 3credits",
                           "DESN220 - Online - Elon Musk - S 2:00pm-5:30pm - Franklin - 16Wks - 3credits"]

                CourseFrame.__init__(self, parent, controller, course_name="DESN 220", course_list=course_list, course_index=3)


class Engr195Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["ENGR195 - Online - Henry Ford - T,R 8:00pm-10:00pm - Plainfield - 16Wks - 3credits",
                          "ENGR195 - Virtual - Nikola Tesla - W 1:00pm-3:50pm - Columbus - 8Wks - 3credits",
                          "ENGR195 - Traditional - Alexander Graham Bell - M,F 9:00am-11:00am - Muncie - 16Wks - 3credits"]

                CourseFrame.__init__(self, parent, controller, course_name="ENGR 195", course_list=course_list, course_index=4)


class Hvac171Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["HVAC170 - Traditional - Willis Carrier - T,R 2:00pm-4:00pm - Plainfield - 16Wks - 3credits",
                          "HVAC170 - Virtual - Diana Prince - W 3:00pm-5:50pm - Themyscira - 8Wks - 3credits",
                          "HVAC170 - Virtual - Jon Snow - M,F 11:00am-1:00pm - Salt Lake City - 16Wks - 3credits"]

                CourseFrame.__init__(self, parent, controller, course_name="HVAC 171", course_list=course_list, course_index=5)


class Legs170Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["LEGS170 - Virtual - Camilla Vasquez Ford - F 8:00am-12:00pm - Albany - 16Wks - 3credits",
                          "LEGS170 - Online - Johnnie Cochran - W 1:00pm-5:00pm - New York City - 16Wks - 3credits",
                          "LEGS170 - Virtual - Analise Keating - M 3:00pm-7:00pm - Minneapolis - 16Wks - 3credits"]

                CourseFrame.__init__(self, parent, controller, course_name="LEGS 170", course_list=course_list, course_index=6)


class Math137Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["MATH137 - Anywhere - Keneisha E - M,TH 9:00am-1:00pm - FortWayne - 16Wks - 3 credits",
                           "MATH137 - Online - Milford Hutsell - M,W 6:00pm-8:50pm - Columbus - 2nd 8Wks - 3credits",
                           "MATH137 - Traditional - Mike Gorsline - m,w 2:00pm-5:00pm - N Meridian - 1st 8Wks - 3credits"]

                CourseFrame.__init__(self, parent, controller, course_name="MATH 137", course_list=course_list, course_index=7)


class Sdev220Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["SDEV220 - Virtual - Feihong Liu - M,W 3:00pm-5:50pm - FortWayne - 8Wks - 3 credits", 
                               "SDEV220 - Online - Tim Tim - TH,M 6:00pm-8:50pm - Columbus - 16Wks - 3 credits", 
                               "SDEV220 - Virtual - Tom Tom - TU,W 1:00pm-4:00pm - N Meridian - 8Wks - 3 credits"]

                CourseFrame.__init__(self, parent, controller, course_name="SDEV 220", course_list=course_list, course_index=8)


if __name__ == "__main__":
    print('please run the main.py file instead')