"""
Course Manager
07/24/2022
version 3.0
Author:  ['Yahya G. Alrobaie', 'Gunnar Dahl', 'Alvin Hampton','Shanika N. Person']
Course Manager GUI App
This program allows users to view and enroll in college courses.
GUI includes: 
- Login window that authenticates users
- Course tab that allows the user to view and select courses to enroll in
- Schedule tab that allows the user to view the courses they are enrolled in
"""
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import  Frame, ttk

# Creat names and pin for the users to login {"username":"Pin"}
database = {"yahya": "1111", "gunnar": "2222", "alvin": "3333", "shanika": "4444"}
print(database)


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

#the container is where we'll stackabunch of frames
#on top of each other, then the one we want visible
#will be raised above the others
        self.shared_data = {'StartPage':tk.StringVar()}
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, CoursesPage, Acct101Page, Bio101Page, Dbms110Page, Desn220Page, Engr195Page, Hvac171Page, Legs170Page, Math137Page, Sdev220Page):
            page_name = F.__name__
            frame = F(parent=container, controller= self)
            self.frames[page_name] = frame
            
#put all of the pages in the same location;
#the one on the top of the stacking order
#will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame=self.frames[page_name]
        frame.tkraise()

#+++++++++++++++++++++++++
# the StartPage class which hold the login screen
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

# the Frame that control everything we add th the page
        tk.Frame.__init__(self, parent, background='#003366')
        self.controller=controller
        
        self.controller.title('Ivy Courses Registration')
# options for the screen size normal, iconic, withdrawn, or zoomed
        self.controller.state('normal')

# Creat a function to clear the entries Widget conten
        def clear_text():
            user_entry_Box.delete(0, tk.END)
            pin_entry_Box.delete(0, tk.END)

# Creat a Notebook(tabs) for the CoursesPage.
        my_notebook = ttk.Notebook(self, width=638, height=395)
        my_notebook.pack()
# Creat a frames inside the notebook
        my_frame = Frame(my_notebook, bg="#003366",)
        my_frame.pack()
        my_notebook.add(my_frame, text="Login")

 #+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the login page
        header_label1 = tk.Label(my_frame, text="IVY Courses Registration", foreground='White',width=600, background='#660066', font=('bold', 45))
        header_label1.pack()

        selection_label1= tk.Label(my_frame, text="Login to Your Account:", fg='white',font=('bold',20), background='#003366' ,anchor='w')
        selection_label1.place(x=0, y=60)


# +++++++++++++++++++++++++++
# Creat a pin Label to ask the user to enter the username
        user_label = tk.Label(my_frame, text='Enter your Username:', font=15, background='#003366')
        user_label.place(x=8,y=150)
# Creat a entery box, to put the username
        user = tk.StringVar()      
        user_entry_Box = tk.Entry(my_frame, textvariable=user)
        user_entry_Box.focus_set()
        user_entry_Box.place(x=170, y=150)


#++++++++++++++++++++++++++++ #336699
# Creat a pin Label to ask the user to enter the pin 
        pin_label = tk.Label(my_frame, text='Enter your PIN number:', font=15, background='#003366')
        pin_label.place(x=8,y=190) 
# Creat a entery box, to put the pin
        pin = tk.StringVar()      
        pin_entry_Box = tk.Entry(my_frame, textvariable=pin)
        pin_entry_Box.place(x=170,y=190)


# Creat a login function to check the user validate, and the user login
        def login_check():
            global database
            if user.get() in database :
                if database[user.get()] == pin.get() :
                        pin.set('')  
                        user.set('')
                        incorrect_login_label['text']=''
                        controller.show_frame('CoursesPage')
                else:
                        incorrect_login_label['text']='Incorrect User or PIN'
            elif pin.get() == '' and user.get() == '':
                    incorrect_login_label['text']=' Login please'
            else:
                incorrect_login_label['text']='Incorrect User or PIN'

        
# creat a Enter Button
        enter_button = tk.Button(my_frame, text='Enter', command=login_check, relief='raised', width=10,height=2, borderwidth=3, )
        enter_button.place(x=45, y=270)

# creat a Clear Button to Clear the login text
        button_clear = tk.Button(my_frame, text="Clear", command=clear_text,relief='raised',width=10,height=2, borderwidth=3)
        button_clear.place(x=230, y=270 )

# creat a Exit Button to quit the program
        button_quit = tk.Button(my_frame, text="Exit", command=self.quit,relief='raised', width=10,height=2, borderwidth=3)
        button_quit.place(x=420, y=270)

# Creat a display message when the user enter the incorrect login # foreground='#990033'
        incorrect_login_label = tk.Label(my_frame, text="", background='#003366', font=('bold', 22),anchor='n' )
        incorrect_login_label.place(x=180, y=220)


#+++++++++++++++++++++++
# Creat class to the second window( CoursesPage)
class CoursesPage(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, background='#660066')
            self.controller=controller


# Creat a Notebook(tabs) for the CoursesPage.
            my_notebook = ttk.Notebook(self,width=638, height=395)
            my_notebook.pack()

# Creat a frames inside the notebook
            my_frame1 = Frame(my_notebook, bg="#003366",)
            my_frame1.pack()

            global my_frame2
            my_frame2 = Frame(my_notebook, bg="#003366")
            my_frame2.pack()

# Display the name of the frames
            my_notebook.add(my_frame1, text="Courses")
            my_notebook.add(my_frame2, text="Schedule")


#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the CoursesPage
            header_label3 = tk.Label(my_frame1, text="IVY Courses", foreground='White', width=600, background='#660066', font=('bold', 30))
            header_label3.pack()

            selection_label= tk.Label(my_frame1, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
            selection_label.place(x=0, y=40)
  
# ++++++++++++++++++++++++++++
# Creat a acct_101 function to move to the acct_101 window 
            def acct_101():
                controller.show_frame('Acct101Page')

# Creat a acct_101 button
            acct101_button = tk.Button(my_frame1, text="ACCT101", command=acct_101, relief='raised', borderwidth=3, width=20, height=4,)
            acct101_button.place(x=0, y=100)

# ++++++++++++++++++++++++++++
# Creat a bio_101 function to move to the bio_101 window 
            def bio_101():
                controller.show_frame('Bio101Page')

# Creat a bio_101 button
            bio101_button = tk.Button(my_frame1, text="BIO101", command=bio_101, relief='raised', borderwidth=3, width=20, height=4)
            bio101_button.place(x=215, y=100)

# ++++++++++++++++++++++++++++
# Creat a dbms_110 function to move to the dbms_110 window 
            def dbms_110():
                controller.show_frame('Dbms110Page')
# Creat a dbms_110 button
            dbms110_button = tk.Button(my_frame1, text="DBMS110", command=dbms_110, relief='raised', borderwidth=3, width=20, height=4)
            dbms110_button.place(x=420, y=100)

# ++++++++++++++++++++++++++++
# Creat a desn_220 function to move to the desn_220 window 
            def desn_220():
                controller.show_frame('Desn220Page')
# Creat a desn_220 button
            desn220_button = tk.Button(my_frame1, text="DESN220", command=desn_220, relief='raised', borderwidth=3,width=20, height=4)
            desn220_button.place(x=0, y=178)

# ++++++++++++++++++++++++++++
# Creat a engr_195 function to move to the engr_195 window 
            def engr_195():
                controller.show_frame('Engr195Page')
# Creat a engr_195 button
            engr195_button = tk.Button(my_frame1, text="ENGR195", command=engr_195, relief='raised', borderwidth=3,width=20, height=4)
            engr195_button.place(x=215, y=178)

# ++++++++++++++++++++++++++++
# Creat a hvac_171 function to move to the hvac_171 window 
            def hvac_171():
                controller.show_frame('Hvac171Page')
# Creat a hvac_171 button
            hvac171_button = tk.Button(my_frame1, text="HVAC171", command=hvac_171, relief='raised', borderwidth=3,width=20, height=4)
            hvac171_button.place(x=420, y=178)

# ++++++++++++++++++++++++++++
# Creat a legs_170 function to move to the legs_170 window 
            def legs_170():
                controller.show_frame('Legs170Page')
# Creat a engr_195 button
            legs170_button = tk.Button(my_frame1, text="LEGS170", command=legs_170, relief='raised', borderwidth=3,width=20, height=4)
            legs170_button.place(x=0, y=256)

# ++++++++++++++++++++++++++++
# Creat a math_137 function to move to the math_137 window 
            def math_137():
                controller.show_frame('Math137Page')
# Creat a math_137 button
            math137_button = tk.Button(my_frame1, text="MATH137", command=math_137, relief='raised', borderwidth=3,width=20, height=4)
            math137_button.place(x=215, y=256)

            # ++++++++++++++++++++++++++++
# Creat a sdev_220 function to move to the sdev_220 window 
            def sdev_220():
                controller.show_frame('Sdev220Page')
# Creat a sdev_220 button
            sdev220_button = tk.Button(my_frame1, text="SDEV220", command=sdev_220, relief='raised', borderwidth=3,width=20, height=4)
            sdev220_button.place(x=420, y=256)


# ++++++++++++++++++++++++++++
# Creat a exit function
            def logout():
                controller.show_frame('StartPage')
# Creat a exit button
            exit_button = tk.Button(my_frame1, text="Logout", command=logout, relief='raised', width=10, height=2, borderwidth=2)
            exit_button.place(x=515, y=0)



#+++++++++++++++++++++++++++++
# Creat class to the Acct101Page window.
class Acct101Page (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Acct101Page.
        acct101_notebook = ttk.Notebook(self, width=638, height=395)
        acct101_notebook.pack()
# Creat a frames inside the notebook
        my_frame3 = Frame(acct101_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        acct101_notebook.add(my_frame3, text="ACCT101")
        

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Sdev153Page page
        selection_label2= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label2.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_acct101_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_acct101_listbox.place(x=0, y= 30)

# Add list of items
        my_acct101_list = ["ACCT101 - Virtual - Sean Carter - M,W 10:00am-12:00pm - FortWayne - 8Wks - 3credit",
                           "ACCT101 - Learn Anywhere - Kim Kardashian - T,R 1:00pm-3:00pm - Columbus - 16Wks - 3credit",
                           "ACCT101 - Traditional - Curtis Jackson - F 3:00pm-6:00pm - N Meridian - 8Wks - 3credit"]
        
        for acct101_itme in my_acct101_list:
            my_acct101_listbox.insert(tk.END, acct101_itme)

# Creat an uneroll function
        def unenroll():
            my_acct101_label.config(text='')
            schedule_acct101_label.config(text='')
            acct101_enroll_button['state']= tk.NORMAL
            acct101_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_acct101_label.config(text=my_acct101_listbox.get(ANCHOR))
            schedule_acct101_label.config(text=my_acct101_listbox.get(ANCHOR))
            acct101_enroll_button['state']= tk.DISABLED
            acct101_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        acct101_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        acct101_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        acct101_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        acct101_unenroll_button.place(x=229, y=180)
        acct101_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_acct101_label
        my_acct101_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_acct101_label.place(x=7, y=120)

        global schedule_acct101_label
        schedule_acct101_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_acct101_label.place(x=7,  y=2)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)


#++++++++++++++++++++++++++
# Creat class to the Bio101Page window.
class Bio101Page (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Bio101Page.
        bio101_notebook = ttk.Notebook(self, width=638, height=395)
        bio101_notebook.pack()
# Creat a frames inside the notebook
        my_frame3 = Frame(bio101_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        bio101_notebook.add(my_frame3, text="BIO101")
        

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Bio101Page page
        selection_label3= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label3.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_bio101_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_bio101_listbox.place(x=0, y= 30)

# Add list of items
        my_bio101_list = ["BIO101 - Traditional - Nye Bill  - M,W 1:00pm-4:30pm - FortWayne - 8Wks - 3credit",
                          "BIO101 - Virtual - Professor X - T,R 6:00pm-9:30pm - Columbus - 16Wks - 3credit",
                          "BIO101 - Traditional - Bill Nye - T 1:00pm-5:00pm - N Meridian - 8Wks - 3credit"]

        
        for bio101_itme in my_bio101_list:
            my_bio101_listbox.insert(tk.END, bio101_itme)

# Creat an uneroll function
        def unenroll():
            my_bio101_label.config(text='')
            schedule_bio101_label.config(text='')
            bio101_enroll_button['state']= tk.NORMAL
            bio101_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_bio101_label.config(text=my_bio101_listbox.get(ANCHOR))
            schedule_bio101_label.config(text=my_bio101_listbox.get(ANCHOR))
            bio101_enroll_button['state']= tk.DISABLED
            bio101_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        bio101_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        bio101_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        bio101_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        bio101_unenroll_button.place(x=229, y=180)
        bio101_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_bio101_label
        my_bio101_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_bio101_label.place(x=7, y=120)

        global schedule_bio101_label
        schedule_bio101_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_bio101_label.place(x=7,  y=47)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)


# Creat class to the Dbms110Page window.
class Dbms110Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Dbms110Page.
        dbms110_notebook = ttk.Notebook(self, width=638, height=395)
        dbms110_notebook.pack()
# Creat a frames inside the notebook
        my_frame3 = Frame(dbms110_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        dbms110_notebook.add(my_frame3, text="DBMS110")
        
        

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Dbms110Page page
        selection_label3= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label3.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_dbms110_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_dbms110_listbox.place(x=0, y= 30)

# Add list of items
        my_dbms110_list = ["DBMS110 - Traditional - Anthony Stark - F 2:00pm-5:50pm - New York City - 16Wks - 3credit",
                          "DBMS110 - Virtual -  Stark Anthony - T,R 2:00pm-3:50pm - New York City - 8Wks - 3credit",
                          "DBMS110 - Traditional - Bruce Wayne - S 9:00am-12:50pm - Gotham - 16Wks - 3credit"]
        
        for dbms110_itme in my_dbms110_list:
            my_dbms110_listbox.insert(tk.END, dbms110_itme)

# Creat an uneroll function
        def unenroll():
            my_dbms110_label.config(text='')
            schedule_dbms110_label.config(text='')
            dbms110_enroll_button['state']= tk.NORMAL
            dbms110_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_dbms110_label.config(text=my_dbms110_listbox.get(ANCHOR))
            schedule_dbms110_label.config(text=my_dbms110_listbox.get(ANCHOR))
            dbms110_enroll_button['state']= tk.DISABLED
            dbms110_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        dbms110_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        dbms110_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        dbms110_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        dbms110_unenroll_button.place(x=229, y=180)
        dbms110_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_dbms110_label
        my_dbms110_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_dbms110_label.place(x=7, y=120)

        global schedule_dbms110_label
        schedule_dbms110_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_dbms110_label.place(x=7,  y=92)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)

# Creat class to the Desn220Page window.
class Desn220Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Desn220Page.
        desn220_notebook = ttk.Notebook(self, width=638, height=395)
        desn220_notebook.pack()
# Creat a frames inside the notebook
        my_frame3 = Frame(desn220_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        desn220_notebook.add(my_frame3, text="DESN220")
        
        

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Desn220Page page
        selection_label5= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label5.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_desn220_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_desn220_listbox.place(x=0, y= 30)

# Add list of items
        my_desn220_list = ["DESN220 - Anywhere - Mark Zuckerberg - F 1:00pm-4:30pm - Plainfield - 16Wks - 3credit",
                           "DESN220 - Traditional - Steve Jobs Jr. - T,R 6:00pm-7:30pm - Indianapolis - 8Wks - 3credit",
                           "DESN220 - Online - Elon Musk - S 2:00pm-5:30pm - Franklin - 16Wks - 3credit"]

        
        for desn220_itme in my_desn220_list:
            my_desn220_listbox.insert(tk.END, desn220_itme)

# Creat an uneroll function
        def unenroll():
            my_desn220_label.config(text='')
            schedule_desn220_label.config(text='')
            desn220_enroll_button['state']= tk.NORMAL
            desn220_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_desn220_label.config(text=my_desn220_listbox.get(ANCHOR))
            schedule_desn220_label.config(text=my_desn220_listbox.get(ANCHOR))
            desn220_enroll_button['state']= tk.DISABLED
            desn220_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        desn220_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        desn220_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        desn220_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        desn220_unenroll_button.place(x=229, y=180)
        desn220_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_desn220_label
        my_desn220_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_desn220_label.place(x=7, y=120)

        global schedule_desn220_label
        schedule_desn220_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_desn220_label.place(x=7,  y=136)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)

# Creat class to the Engr195Page window.
class Engr195Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Engr195Page.
        engr195_notebook = ttk.Notebook(self, width=638, height=395)
        engr195_notebook.pack()
# Creat a frames inside the notebook
        my_frame3 = Frame(engr195_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        engr195_notebook.add(my_frame3, text="ENGR195")
        
#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Engr195Page page
        selection_label6= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label6.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_engr195_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_engr195_listbox.place(x=0, y= 30)

# Add list of items
        my_engr195_list =["ENGR195 - Online - Henry Ford - T,R 8:00pm-10:00pm - Plainfield - 16Wks - 3credit",
                          "ENGR195 - Virtual - Nikola Tesla - W 1:00pm-3:50pm - Columbus - 8Wks - 3credit",
                          "ENGR195 - Traditional - Alexander Graham Bell - M,F 9:00am-11:00am - Muncie - 16Wks - 3credit"]

        
        for engr195_itme in my_engr195_list:
            my_engr195_listbox.insert(tk.END, engr195_itme)

# Creat an uneroll function
        def unenroll():
            my_engr195_label.config(text='')
            schedule_engr195_label.config(text='')
            engr195_enroll_button['state']= tk.NORMAL
            engr195_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_engr195_label.config(text=my_engr195_listbox.get(ANCHOR))
            schedule_engr195_label.config(text=my_engr195_listbox.get(ANCHOR))
            engr195_enroll_button['state']= tk.DISABLED
            engr195_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        engr195_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        engr195_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        engr195_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        engr195_unenroll_button.place(x=229, y=180)
        engr195_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_engr195_label
        my_engr195_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_engr195_label.place(x=7, y=120)

        global schedule_engr195_label
        schedule_engr195_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_engr195_label.place(x=7,  y=180)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)

# Creat class to the Hvac171Page window.
class Hvac171Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Hvac171Page.
        hvac171_notebook = ttk.Notebook(self, width=638, height=395)
        hvac171_notebook.pack()
# Creat a frames inside the notebook.
        my_frame3 = Frame(hvac171_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        hvac171_notebook.add(my_frame3, text="HVAC171")
        
#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Hvac171Page page
        selection_label7= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label7.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_hvac171_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_hvac171_listbox.place(x=0, y= 30)

# Add list of items
        my_hvac171_list =["HVAC170 - Traditional - Willis Carrier - T,R 2:00pm-4:00pm - Plainfield - 16Wks - 3credit",
                          "HVAC170 - Virtual - Diana Prince - W 3:00pm-5:50pm - Themyscira - 8Wks - 3credit",
                          "HVAC170 - Virtual - Jon Snow - M,F 11:00am-1:00pm - Salt Lake City - 16Wks - 3credit"]
        
        for hvac171_itme in my_hvac171_list:
            my_hvac171_listbox.insert(tk.END, hvac171_itme)

# Creat an uneroll function
        def unenroll():
            my_hvac171_label.config(text='')
            schedule_hvac171_label.config(text='')
            hvac171_enroll_button['state']= tk.NORMAL
            hvac171_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_hvac171_label.config(text=my_hvac171_listbox.get(ANCHOR))
            schedule_hvac171_label.config(text=my_hvac171_listbox.get(ANCHOR))
            hvac171_enroll_button['state']= tk.DISABLED
            hvac171_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        hvac171_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        hvac171_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        hvac171_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        hvac171_unenroll_button.place(x=229, y=180)
        hvac171_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_hvac171_label
        my_hvac171_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_hvac171_label.place(x=7, y=120)

        global schedule_hvac171_label
        schedule_hvac171_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_hvac171_label.place(x=7,  y=222)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)


# Creat class to the Legs170Page window.
class Legs170Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Legs170Page.
        legs170_notebook = ttk.Notebook(self, width=638, height=395)
        legs170_notebook.pack()
# Creat a frames inside the notebook.
        my_frame3 = Frame(legs170_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        legs170_notebook.add(my_frame3, text="LEGS170")
        
        

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Legs170Page page
        selection_label8= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label8.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_legs170_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_legs170_listbox.place(x=0, y= 30)

# Add list of items
        my_legs170_list =["LEGS170 - Virtual - Camilla Vasquez Ford - F 8:00am-12:00pm - Albany - 16Wks - 3credit",
                          "LEGS170 - Online - Johnnie Cochran - W 1:00pm-5:00pm - New York City - 16Wks - 3credit",
                          "LEGS170 - Virtual - Analise Keating - M 3:00pm-7:00pm - Minneapolis - 16Wks - 3credit"]
        
        for legs170_itme in my_legs170_list:
            my_legs170_listbox.insert(tk.END, legs170_itme)

# Creat an uneroll function
        def unenroll():
            my_legs170_label.config(text='')
            schedule_legs170_label.config(text='')
            legs170_enroll_button['state']= tk.NORMAL
            legs170_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_legs170_label.config(text=my_legs170_listbox.get(ANCHOR))
            schedule_legs170_label.config(text=my_legs170_listbox.get(ANCHOR))
            legs170_enroll_button['state']= tk.DISABLED
            legs170_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        legs170_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        legs170_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        legs170_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        legs170_unenroll_button.place(x=229, y=180)
        legs170_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_legs170_label
        my_legs170_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_legs170_label.place(x=7, y=120)

        global schedule_legs170_label
        schedule_legs170_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_legs170_label.place(x=7,  y=264)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)

# Creat class to the Math137Page window.
class Math137Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Math137Page.
        math137_notebook = ttk.Notebook(self, width=638, height=395)
        math137_notebook.pack()
# Creat a frames inside the notebook.
        my_frame3 = Frame(math137_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        math137_notebook.add(my_frame3, text="MATH137")
        
        

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Math137Page page
        selection_label9= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label9.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_math137_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_math137_listbox.place(x=0, y= 30)

# Add list of items
        my_math137_list = ["MATH137 - Anywhere - Keneisha E - M,TH 9:00am-1:00pm - FortWayne - 16Wks - 3 credits",
                           "MATH137 - Online - Milford Hutsell - M,W 6:00pm-8:50pm - Columbus - 2nd 8Wks - 3credits",
                           "MATH137 - Traditional - Mike Gorsline - m,w 2:00pm-5:00pm - N Meridian - 1st 8Wks - 3credits"]
        
        for math137_itme in my_math137_list:
            my_math137_listbox.insert(tk.END, math137_itme)

# Creat an uneroll function
        def unenroll():
            my_math137_label.config(text='')
            schedule_math137_label.config(text='')
            math137_enroll_button['state']= tk.NORMAL
            math137_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_math137_label.config(text=my_math137_listbox.get(ANCHOR))
            schedule_math137_label.config(text=my_math137_listbox.get(ANCHOR))
            math137_enroll_button['state']= tk.DISABLED
            math137_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        math137_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        math137_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        math137_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        math137_unenroll_button.place(x=229, y=180)
        math137_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_math137_label
        my_math137_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_math137_label.place(x=7, y=120)

        global schedule_math137_label
        schedule_math137_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_math137_label.place(x=7,  y=307)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)

# Creat class to the Sdev220Page window.
class Sdev220Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++

# Creat a Notebook(tabs) for the Sdev220Page.
        sdev220_notebook = ttk.Notebook(self, width=638, height=395)
        sdev220_notebook.pack()
# Creat a frames inside the notebook.
        my_frame3 = Frame(sdev220_notebook, bg="#003366",)
        my_frame3.pack()

# Display the name of the frames
        sdev220_notebook.add(my_frame3, text="SDEV220")
        
        

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the Sdev220Page page
        selection_label10= tk.Label(my_frame3, text="Select a course to enroll:", fg='white', background='#003366',font=('bold',20) ,anchor='w')
        selection_label10.place(x=0, y=0)
  
# +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED
        bolded = font.Font(weight='bold')
        my_sdev220_listbox = tk.Listbox(my_frame3,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_sdev220_listbox.place(x=0, y= 30)

# Add list of items
        my_sdev220_list = ["SDVE220 - Virtual - Feihong Liu - M,W 3:00pm-5:50pm - FortWayne - 8Wks - 3credit", 
                           "SDVE220 - Online - Tim Tom  - TH,M 6:00pm-8:50pm - Columbus - 16Wks - 3credit", 
                           "SDVE220 - Anywhere - Tom Tim  - TU,W 1:00pm-4:00pm - N Meridian - 8Wks - 3credit"]
        
        for sdev220_itme in my_sdev220_list:
            my_sdev220_listbox.insert(tk.END, sdev220_itme)

# Creat an uneroll function
        def unenroll():
            my_sdev220_label.config(text='')
            schedule_sdev220_label.config(text='')
            sdev220_enroll_button['state']= tk.NORMAL
            sdev220_unenroll_button['state']= tk.DISABLED

# Creat an enroll function
        def enroll():
            my_sdev220_label.config(text=my_sdev220_listbox.get(ANCHOR))
            schedule_sdev220_label.config(text=my_sdev220_listbox.get(ANCHOR))
            sdev220_enroll_button['state']= tk.DISABLED
            sdev220_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        sdev220_enroll_button = tk.Button(my_frame3, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        sdev220_enroll_button.place(x=40, y=180)

# Creat a uneroll button
        sdev220_unenroll_button = tk.Button(my_frame3, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        sdev220_unenroll_button.place(x=229, y=180)
        sdev220_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_sdev220_label
        my_sdev220_label = tk.Label(my_frame3, text='Enrolled class will appear here ', background='#333333', borderwidth=5, relief='raised',width=65,height=2,)
        my_sdev220_label.place(x=7, y=120)

        global schedule_sdev220_label
        schedule_sdev220_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=65,height=2,)
        schedule_sdev220_label.place(x=7,  y=350)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(my_frame3, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=420, y=180)

#++++++++++++++++++++++++++++++
# to display everything
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


