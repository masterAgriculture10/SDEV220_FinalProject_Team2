"""
Course Manager GUI App

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
                for Frame in (StartPage, CoursesPage, Sdev153Page, Sdev140Page, Sdev220Page):
                        page_name = Frame.__name__
                        frame = Frame(parent=container, controller=self)
                        self.frames[page_name] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
                        self.show_frame("StartPage")
        

        def show_frame(self, page_name):
                '''Show a frame for the given page name'''
                frame=self.frames[page_name]
                frame.tkraise()



# hex color constants
COURSE_HEADING_COL     = '#660066'
SELECT_LBL_COL         = '#003366'
COURSE_PAGE_BG_COL     = '#336699'
ENROLLED_LBL_COL       = '#999999'
COURSES_TAB_HEADER_COL = '#043927'


class StartPage(tk.Frame):
        """A frame that contains the elements of the login screen"""
        def __init__(self, parent, controller):
                # the Frame that controls everything we add to the page
                tk.Frame.__init__(self, parent, background='#003366')
                self.controller=controller
                
                self.controller.title('SDEV Courses Registration')
                # options for the screen size: normal, iconic, withdrawn, or zoomed
                self.controller.state('normal')


                # header labels
                header_label1 = tk.Label(self, text="SDEV Courses Registration", foreground='White', background='#336699', font=('bold', 50))
                header_label1.pack()

                header_label2 = tk.Label(self, text="Login to Your Account", foreground='White', background='#336699', font=('bold', 50))
                header_label2.pack(pady=30)

                # label for spacing
                space_label = tk.Label(self, height=5, background='#003366')
                space_label.pack()


                # username label & entry box
                user_label = tk.Label(self, text='Enter your username:', font=15, background='#003366')
                user_label.place(x=8,y=180)

                username = tk.StringVar()      
                username_entry_box = tk.Entry(self, textvariable=username)
                username_entry_box.focus_set()
                username_entry_box.place(x=170, y=180)


                # password label & entry box
                password_label = tk.Label(self, text='Enter your password:', font=15, background='#003366')
                password_label.place(x=8,y=210) 

                password = tk.StringVar()      
                password_entry_box = tk.Entry(self, textvariable=password)
                password_entry_box.place(x=170,y=210)


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
                submit_button = tk.Button(self, text='Submit', command=login_check, relief='flat', width=10)
                submit_button.place(x=10, y=250)

                quit_button = tk.Button(self, text="Exit", command=self.quit,relief='flat', width=10)
                quit_button.place(x=180, y=250)

                clear_button = tk.Button(self, text="Clear", command=clear_text,relief='flat', width=10)
                clear_button.place(x=350, y=250)


                # create a message label to display when the user enters an incorrect login 
                incorrect_login_label = tk.Label(self, text="", background='#336699', foreground='#990033', font=('bold', 22), anchor='n')
                incorrect_login_label.pack(fill='both', expand=True)




class CoursesPage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent, background=COURSE_HEADING_COL)
                self.controller=controller


                # create a notebook and its tab frames
                notebook = ttk.Notebook(self)
                notebook.pack(fill="both", expand=1)

                courses_tab = Frame(notebook, bg=SELECT_LBL_COL)
                courses_tab.pack(fill="both", expand=1)

                schedule_tab = Frame(notebook, bg="green")
                schedule_tab.pack(fill="both", expand=1)

                notebook.add(courses_tab, text="Courses")
                notebook.add(schedule_tab, text="Schedule")
                

                # labels for the courses tab
                courses_header_lbl = tk.Label(courses_tab, text="IVY SDVE Courses", foreground='White', background=COURSES_TAB_HEADER_COL, font=('bold', 50))
                courses_header_lbl.pack(fill="both", expand=1)

                courses_subheader_lbl = tk.Label(courses_tab, text="Courses", foreground='White', background=COURSES_TAB_HEADER_COL, font=('bold', 30))
                courses_subheader_lbl.pack(fill="both", expand=1)

                selection_lbl= tk.Label(courses_tab, text="Select a course to enroll", fg='white', background=SELECT_LBL_COL, anchor='w')
                selection_lbl.pack(fill='x')


                # make course buttons using a for loop
                # (button text, class name, args for pack)
                button_values = (
                        ('SDEV 153', 'Sdev153Page', {'side':'left'}),
                        ('SDEV 140', 'Sdev140Page', {'side':'right'}),
                        ('SDEV 220', 'Sdev220Page', {'side':'left', 'fill':'x', 'expand':0}),
                )

                for (button_text, cls_name, pack_args) in button_values:
                        withdraw_button = tk.Button(courses_tab, text=button_text, 
                                                    command=lambda:controller.show_frame(cls_name), 
                                                    relief='raised', borderwidth=3, width=25, height=5)
                        withdraw_button.pack(**pack_args)


                # make an exit button                
                exit_button = tk.Button(courses_tab, text="Log Out", 
                                        command=lambda:controller.show_frame('StartPage'), 
                                        relief='raised', borderwidth=3,width=25, height=5)
                exit_button.pack(side="bottom")



class CourseFrame(tk.Frame):
        """Base class for creating course frames"""

        def __init__(self, parent, controller, course_name, course_list):
                tk.Frame.__init__(self, parent, background=COURSE_HEADING_COL)
                self.controller=controller


                # header label
                header_lbl = tk.Label(self, text=course_name, foreground='white', background=COURSE_HEADING_COL, font=('bold', 50))
                header_lbl.pack()

                select_lbl = tk.Label(self, text="Select a class to enroll in: ", foreground='white', background=SELECT_LBL_COL, anchor='w')
                select_lbl.pack(fill='x')


                # put another color on the page using a frame
                button_frame = tk.Frame(self, background=COURSE_PAGE_BG_COL)
                button_frame.pack(fill='both', expand=True)


                # listbox
                bold_font = font.Font(weight='bold')
                course_listbox = tk.Listbox(button_frame,font=bold_font, relief='raised', borderwidth=4, width=70, height=4, selectmode=tk.BROWSE)
                course_listbox.grid(row=0, column=0)
                
                for course in course_list:
                        # add all the courses to the list
                        course_listbox.insert(tk.END, course)


                # enroll & unenroll buttons
                def enroll():
                        enrolled_course_lbl.config(text=course_listbox.get(ANCHOR))
                        enroll_button['state'] = tk.DISABLED
                        unenroll_button['state'] = tk.NORMAL

                def unenroll():
                        enrolled_course_lbl.config(text='')
                        enroll_button['state'] = tk.NORMAL
                        unenroll_button['state'] = tk.DISABLED
                
                enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3, width=15, height=3)
                enroll_button.place(x=3, y=130)

                unenroll_button = tk.Button(button_frame, text="Unenroll", relief='raised', command=unenroll, borderwidth=3, width=15, height=3)
                unenroll_button.place(x=179, y=130)
                unenroll_button['state'] = tk.DISABLED


                # display the enrolled class
                enrolled_course_lbl = tk.Label(button_frame, text='Enrolled class will appear here.', background=ENROLLED_LBL_COL, 
                                               borderwidth=5, relief='raised', width=70, height=2)
                enrolled_course_lbl.place(x=3, y=80)


                # back button
                def back():
                        controller.show_frame('CoursesPage')

                back_button = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15, height=3)
                back_button.place(x=355, y=130)


# CourseFrame child classes

class Sdev153Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["SDVE153 - Anywhere - Keneisha E - M,TH 9:00am-1:00pm - FortWayne - 16Wks - 3 credits", 
                               "SDVE153 - Online - Milford Hutsell - M,W 6:00pm-8:50pm - Columbus - 2nd 8Wks - 3credits", 
                               "SDVE153 - Traditional - Mike Gorsline - m,w 2:00pm-5:00pm - N Meridian - 1st 8Wks - 3credits"]

                super().__init__(parent, controller, course_name="SDEV 153", course_list=course_list)


class Sdev140Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["SDVE140 - Anywhere - Steve Carver - M,W 1:00pm-4:50pm - FortWayne - 16Wks - 3 credits", 
                               "SDVE140 - Online - Jon Jon - M,W 6:00pm-8:50pm - Columbus - 16Wks - 3credits", 
                               "SDVE140 - Virtual - Alf Sanford - F,M 1:00pm-4:00pm - N Meridian - 8Wks - 3credits"]

                super().__init__(parent, controller, course_name="SDEV 140", course_list=course_list)


class Sdev220Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["SDEV220 - Virtual - Feihong Liu - M,W 3:00pm-5:50pm - FortWayne - 8Wks - 3 credits", 
                               "SDEV220 - Online - Tim Tim - TH,M 6:00pm-8:50pm - Columbus - 16Wks - 3 credits", 
                               "SDEV220 - Virtual - Tom Tom - TU,W 1:00pm-4:00pm - N Meridian - 8Wks - 3 credits"]

                super().__init__(parent, controller, course_name="SDEV 220", course_list=course_list)



# display everything
if __name__ == "__main__":
    CourseApp().mainloop()