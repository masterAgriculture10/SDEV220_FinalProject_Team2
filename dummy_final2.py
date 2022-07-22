# ')from cgitb import text
from faulthandler import disable
import tkinter as tk
from tkinter import ANCHOR, DISABLED, font

database = {"yahya": "1111", "gunnar": "2222", "alvin": "3333", "shanika": "4444"}
print(database)


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stackabunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.shared_data = {'Balance': tk.IntVar()}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, CoursesPage, Psyc201Page, Sdev153Page, Sdev220Page, Acct101Page, Bio101Page, Csci201Page, Desn220Page, Engr195Page, Hvac171Page, Legs170Page, Math137Page, Neti109Page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


# +++++++++++++++++++++++++
# the StartPage class which hold the login screen
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        # the Frame that control everything we add th the page
        tk.Frame.__init__(self, parent, background='#10570c')
        self.controller = controller

        self.controller.title('ATM')
        # options for the screen size normal, iconic, withdrawn, or zoomed
        self.controller.state('normal')

        # Creat a function to clear the entries Widget conten
        def clear_text():
            user_entry_Box.delete(0, tk.END)
            pin_entry_Box.delete(0, tk.END)

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the login page
        header_label1 = tk.Label(self, text="IVY Course Manager", foreground='White', background='#b5cfb4',
                                 font=('bold', 50))
        header_label1.pack()

        header_label2 = tk.Label(self, text="Login to Your Account", foreground='White', background='#b5cfb4',
                                 font=('bold', 50))
        header_label2.pack(pady=20)
        # Creat a space lable 003366
        space_label = tk.Label(self, height=5, background='#3a453a')
        space_label.pack()

        # ++++++++++++++++++++++++++++
        # Creat a pin Label to ask the user to enter the pin
        user_label = tk.Label(self, text='Enter Username:', font=15, background='#b5cfb4')
        user_label.place(x=8, y=180)

        # Creat a entery box, to put the pin
        user = tk.StringVar()
        user_entry_Box = tk.Entry(self, textvariable=user)
        user_entry_Box.focus_set()
        user_entry_Box.place(x=170, y=180)

        # ++++++++++++++++++++++++++++ #336699
        # Creat a pin Label to ask the user to enter the pin
        pin_label = tk.Label(self, text='Enter your PIN:', font=15, background='#b5cfb4')
        pin_label.place(x=8, y=210)

        # Creat a entery box, to put the pin
        pin = tk.StringVar()
        pin_entry_Box = tk.Entry(self, textvariable=pin)
        pin_entry_Box.place(x=170, y=210)

        # Creat a login function to check the user validate the user login

        def login_check():
            global database
            if user.get() in database:
                if database[user.get()] == pin.get():
                    pin.set('')
                    user.set('')
                    incorrect_login_label['text'] = ''
                    controller.show_frame('CoursesPage')
                else:
                    incorrect_login_label['text'] = 'Incorrect User or PIN'
            elif pin.get() == '' and user.get() == '':
                incorrect_login_label['text'] = ' Login please'
            else:
                incorrect_login_label['text'] = 'Incorrect User or PIN'

        # creat a Enter Button
        enter_button = tk.Button(self, text='Enter', command=login_check, relief='flat', width=10, )
        enter_button.place(x=10, y=250)

        # creat a Exit Button to quit the program
        button_quit = tk.Button(self, text="Exit", command=self.quit, relief='flat', width=10, )
        button_quit.place(x=180, y=250)
        # creat a Clear Button to Clear the login text
        button_clear = tk.Button(self, text="Clear", command=clear_text, relief='flat', width=10, )
        button_clear.place(x=350, y=250)

        # Creat a display message when the user enter the incorrect login
        incorrect_login_label = tk.Label(self, text="", background='#336699', foreground='#990033', font=('bold', 22),
                                         anchor='n')
        incorrect_login_label.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++++++
        # Creat a Bottom frame to display the time and the user pin.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


# Creat class to the second window( TransactionPage: Deposit, Withdraw, Balance,Exit)
class CoursesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the TransactionPage page
        header_label3 = tk.Label(self, text="IVY Tech Course Manager", foreground='White', background='#660066',
                                 font=('bold', 50))
        header_label3.pack()

        # Header Labels for the  Header title of the TransactionPage page
        header_label4 = tk.Label(self, text="Courses", foreground='White', background='#660066', font=('bold', 25))
        header_label4.pack(pady=5)

        selection_label = tk.Label(self, text="Select a course to enroll", fg='white', background='#003366', anchor='w')
        selection_label.pack(fill='x')

        # Creat a frame to display the transaction button.
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # ++++++++++++++++++++++++++++
        # Creat a Withdraw function

        # ++++++++++++++++++++++++++++
        # Creat a deposit function
        def psyc_201():
            controller.show_frame('Psyc201Page')

        # Creat a deposit button
        deposit_button = tk.Button(button_frame, text="PSYC201", command=psyc_201, relief='raised', borderwidth=3,
                                   width=25, height=5)
        deposit_button.grid(row=2, column=1)

        # ++++++++++++++++++++++++++++
        # Creat a balance function
        def sdev_220():
            controller.show_frame('Sdev220Page')

        # Creat a balance button
        balance_button = tk.Button(button_frame, text="SDEV220", command=sdev_220, relief='raised', borderwidth=3,
                                   width=25, height=5)
        balance_button.grid(row=2, column=2)

        def acct_101():
            controller.show_frame('Acct101Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="ACCT101", command=acct_101, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=0, column=0)

        def bio_101():
            controller.show_frame('Bio101Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="BIO101", command=bio_101, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=0, column=1)


        def csci_201():
            controller.show_frame('Csci201Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="CSCI201", command=csci_201, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=0, column=2)


        def desn_220():
            controller.show_frame('Desn220Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="DESN220", command=desn_220, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=0, column=3)


        def engr_195():
            controller.show_frame('Engr195Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="ENGR195", command=engr_195, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=1, column=0)
        # ++++++++++++++++++++++++++++

        def hvac_171():
            controller.show_frame('Hvac171Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="HVAC171", command=hvac_171, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=1, column=1)

        def legs_170():
            controller.show_frame('Legs170Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="LEGS170", command=legs_170, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=1, column=2)

        def math_137():
            controller.show_frame('Math137Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="MATH137", command=math_137, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=1, column=3)

        def neti_109():
            controller.show_frame('Math137Page')

        # Creat a withdraw button
        withdraw_button = tk.Button(button_frame, text="NETI109", command=neti_109, relief='raised', borderwidth=3,
                                    width=25, height=5)
        withdraw_button.grid(row=2, column=0)
        # Creat a exit function
        def exit():
            controller.show_frame('StartPage')

        # Creat a exit button

        exit_button = tk.Button(button_frame, text="LogOut", command=exit, relief='raised', borderwidth=3, width=25,
                                height=5)
        exit_button.grid(row=2, column=3, )

        # +++++++++++++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


# +++++++++++++++++++++++++++++
# Creat class to the WithdrawPage window( TransactionPage: Deposit, Withdraw, Balance,Exit)

class Sdev153Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller
        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the WithdrawPage page
        header_label5 = tk.Label(self, text="SDEV153", foreground='White', background='#660066', font=('bold', 50))
        header_label5.pack()

        selection_label2 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label2.pack(fill='x')

        button_frame = tk.Frame(self, background='#336699')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_sdev153_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70, height=4,
                                        selectmode=tk.SINGLE)
        my_sdev153_listbox.grid(row=0, column=0)

        # Add list of items
        my_sdev153_list = ["SDVE153 - Anywhere - Keneisha E - M,TH 9:00am-1:00pm - FortWayne - 16Wks - 3 credits",
                           "SDVE153 - Online - Milford Hutsell - M,W 6:00pm-8:50pm - Columbus - 2nd 8Wks - 3credits",
                           "SDVE153 - Traditional - Mike Gorsline - m,w 2:00pm-5:00pm - N Meridian - 1st 8Wks - 3credits"]

        for sdev153_itme in my_sdev153_list:
            my_sdev153_listbox.insert(tk.END, sdev153_itme)

        # Creat an uneroll function
        def unenroll():
            my_sdev153_label.config(text='')
            sdev153_enroll_button['state'] = tk.NORMAL
            sdev153_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_sdev153_label.config(text=my_sdev153_listbox.get(ANCHOR))
            sdev153_enroll_button['state'] = tk.DISABLED
            sdev153_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev153_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev153_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev153_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev153_unenroll_button.place(x=179, y=130)
        sdev153_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_sdev153_label
        my_sdev153_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_sdev153_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


# ++++++++++++++++++++++++++
# Creat class to the DepositPage window( TransactionPage: Deposit, Withdraw, Balance,Exit)

class Psyc201Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller
        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the DepositPage page
        header_label7 = tk.Label(self, text="Psychology", foreground='White', background='#660066', font=('bold', 50))
        header_label7.pack()

        selection_label3 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label3.pack(fill='x')

        button_frame = tk.Frame(self, background='#336699')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_psyc201_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70, height=4,
                                        selectmode=tk.SINGLE)
        my_psyc201_listbox.grid(row=0, column=0)

        # Add list of items
        my_psyc201_list = ["SDVE140 - Learn Anywhere - Sigmond Freud - M,W 1:00pm-4:50pm - Fort Wayne - 16Wks - 3 credits",
                           "SDVE140 - Traditional - Ivan Pavlov - M,W 6:00pm-8:50pm - Columbus - 16Wks - 3credits",
                           "SDVE140 - Virtual - B.F. Skinner - M,F 1:00pm-4:00pm - N Meridian - 8Wks - 3credits"]

        for psyc201_itme in my_psyc201_list:
            my_psyc201_listbox.insert(tk.END, psyc201_itme)

        # Creat an uneroll function
        def unenroll():
            my_psyc201_label.config(text='')
            sdev140_enroll_button['state'] = tk.NORMAL
            sdev140_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_psyc201_label.config(text=my_psyc201_listbox.get(ANCHOR))
            sdev140_enroll_button['state'] = tk.DISABLED
            sdev140_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev140_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev140_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev140_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev140_unenroll_button.place(x=179, y=130)
        sdev140_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_psyc201_label
        my_psyc201_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_psyc201_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


# Creat class to the class BalancePage window( TransactionPage: Deposit, Withdraw, Balance,Exit)
class Sdev220Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="SDEV220", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colores
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_sdev220_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                             height=4, selectmode=tk.SINGLE)
        my_sdev220_list_listbox.grid(row=0, column=0)

        # Add list of items
        my_sdev220_list = ["SDVE220 - Virtual - Feihong Liu - M,W 3:00pm-5:50pm - FortWayne - 8Wks - 3credit",
                           "SDVE220 - Online - Tim Tim - TH,M 6:00pm-8:50pm - Columbus - 16Wks - 3credit",
                           "SDVE220 - Virtual - Tom Tom - TU,W 1:00pm-4:00pm - N Meridian - 8Wks - 3credit"]

        for sdev220_itme in my_sdev220_list:
            my_sdev220_list_listbox.insert(tk.END, sdev220_itme)

        # Creat an uneroll function
        def unenroll():
            my_sdev220_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_sdev220_label.config(text=my_sdev220_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_sdev220_label
        my_sdev220_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_sdev220_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


class Acct101Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Accounting", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colors
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_sdev220_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                             height=4, selectmode=tk.SINGLE)
        my_sdev220_list_listbox.grid(row=0, column=0)

        # Add list of items
        my_sdev220_list = ["ACCT101 - Virtual - Sean Carter - M,W 10:00am-12:00pm - FortWayne - 8Wks - 3credit",
                           "ACCT101 - Learn Anywhere - Kim Kardashian - T,R 1:00pm-3:00pm - Columbus - 16Wks - 3credit",
                           "ACCT101 - Traditional - Curtis Jackson - F 3:00pm-6:00pm - N Meridian - 8Wks - 3credit"]

        for sdev220_itme in my_sdev220_list:
            my_sdev220_list_listbox.insert(tk.END, sdev220_itme)

        # Creat an uneroll function
        def unenroll():
            my_sdev220_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_sdev220_label.config(text=my_sdev220_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_sdev220_label
        my_sdev220_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_sdev220_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


##NEW CLASS

class Bio101Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Biology", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colores
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_bio101_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                            height=4, selectmode=tk.SINGLE)
        my_bio101_list_listbox.grid(row=0, column=2)

        # Add list of items
        my_bio101_list = ["BIO101 - Traditional - Bill Nye - M,W 1:00pm-4:30pm - FortWayne - 8Wks - 3credit",
                          "BIO101 - Traditional - Professor X - T,R 6:00pm-9:30pm - Columbus - 16Wks - 3credit",
                          "BIO101 - Traditional - Bill Nye - T 1:00pm-5:00pm - N Meridian - 8Wks - 3credit"]

        for bio101_item in my_bio101_list:
            my_bio101_list_listbox.insert(tk.END, bio101_item)

        # Creat an uneroll function
        def unenroll():
            my_bio101_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_bio101_label.config(text=my_bio101_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_bio101_label
        my_bio101_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_bio101_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

#NEW CLASS

class Csci201Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Computer Science", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colores
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_csci201_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                            height=4, selectmode=tk.SINGLE)
        my_csci201_list_listbox.grid(row=0, column=2)

        # Add list of items
        my_csci201_list = ["CSCI201 - Traditional - Mark Zuckerberg - F 1:00pm-4:30pm - Plainfield - 16Wks - 3credit",
                          "CSCI201 - Traditional - Steve Jobs Jr. - T,R 6:00pm-7:30pm - Indianapolis - 8Wks - 3credit",
                          "CSCI201 - Traditional - Elon Musk - S 2:00pm-5:30pm - Franklin - 16Wks - 3credit"]

        for csci201_item in my_csci201_list:
            my_csci201_list_listbox.insert(tk.END, csci201_item)

        # Creat an uneroll function
        def unenroll():
            my_csci201_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_csci201_label.config(text=my_bio101_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_csci201_label
        my_csci201_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_csci201_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

   #NEW CLASS
class Desn220Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Design Technology", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colors
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_desn220_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                            height=4, selectmode=tk.SINGLE)
        my_desn220_list_listbox.grid(row=0, column=2)

        # Add list of items
        my_desn220_list = ["DESN220 - Traditional - Anthony Stark - F 2:00pm-5:50pm - New York City - 16Wks - 3credit",
                          "DESN220 - Traditional - Anthony Stark - T,R 2:00pm-3:50pm - New York City - 8Wks - 3credit",
                          "DESN220 - Traditional - Bruce Wayne - S 9:00am-12:50pm - Gotham - 16Wks - 3credit"]

        for desn220_item in my_desn220_list:
            my_desn220_list_listbox.insert(tk.END, desn220_item)

        # Creat an uneroll function
        def unenroll():
            my_desn220_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_desn220_label.config(text=my_desn220_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_desn220_label
        my_desn220_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_desn220_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

   #NEW CLASS
class Engr195Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Engineering", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colors
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_engr195_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                            height=4, selectmode=tk.SINGLE)
        my_engr195_list_listbox.grid(row=0, column=2)

        # Add list of items
        my_engr195_list = ["ENGR195 - Traditional - Henry Ford - T,R 8:00pm-10:00pm - Plainfield - 16Wks - 3credit",
                          "ENGR195 - Traditional - Nikola Tesla - W 1:00pm-3:50pm - Columbus - 8Wks - 3credit",
                          "ENGR195 - Traditional - Alexander Graham Bell - M,F 9:00am-11:00am - Muncie - 16Wks - 3credit"]

        for engr195_item in my_engr195_list:
            my_engr195_list_listbox.insert(tk.END, engr195_item)

        # Creat an uneroll function
        def unenroll():
            my_engr195_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_engr195_label.config(text=my_engr195_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_engr195_label
        my_engr195_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_engr195_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

   #NEW CLASS
class Hvac171Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Heating and Cooling", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colors
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_hvac171_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                            height=4, selectmode=tk.SINGLE)
        my_hvac171_list_listbox.grid(row=0, column=2)

        # Add list of items
        my_hvac171_list = ["HVAC170 - Traditional - Willis Carrier - T,R 2:00pm-4:00pm - Plainfield - 16Wks - 3credit",
                          "HVAC170 - Virtual - Diana Prince - W 3:00pm-5:50pm - Themyscira - 8Wks - 3credit",
                          "HVAC170 - Traditional - Jon Snow - M,F 11:00am-1:00pm - Salt Lake City - 16Wks - 3credit"]

        for hvac171_item in my_hvac171_list:
            my_hvac171_list_listbox.insert(tk.END, hvac171_item)

        # Creat an uneroll function
        def unenroll():
            my_hvac171_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_hvac171_label.config(text=my_hvac171_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_hvac171_label
        my_hvac171_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_hvac171_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

class Legs170Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Legal Studies", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colors
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_legs170_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                            height=4, selectmode=tk.SINGLE)
        my_legs170_list_listbox.grid(row=0, column=2)

        # Add list of items
        my_legs170_list = ["LEGS170 - Traditional - Camilla Vasquez Ford - F 8:00am-12:00pm - Albany - 16Wks - 3credit",
                          "LEGS170 - Traditional - Johnnie Cochran - W 1:00pm-5:00pm - New York City - 16Wks - 3credit",
                          "LEGS170 - Traditional - Analise Keating - M 3:00pm-7:00pm - Minneapolis - 16Wks - 3credit"]

        for legs170_item in my_legs170_list:
            my_legs170_list_listbox.insert(tk.END, legs170_item)

        # Creat an uneroll function
        def unenroll():
            my_legs170_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_legs170_label.config(text=my_legs170_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_legs170_label
        my_legs170_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_legs170_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

class Math137Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Mathematics", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colors
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_math137_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                            height=4, selectmode=tk.SINGLE)
        my_math137_list_listbox.grid(row=0, column=2)

        # Add list of items
        my_math137_list = ["MATH137 - Virtual - Euclid - W,F 8:00am-10:00am - Greece - 16Wks - 3credit",
                          "MATH137 - Traditional - Leonardo Fibonacci - T,R 3:00pm-5:00pm - Franklin - 16Wks - 3credit",
                          "MATH137 - Learn Anywhere - Isaac Newton - W,R 4:00pm-5:30pm - Indianapolis - 16Wks - 3credit"]

        for math137_item in my_math137_list:
            my_math137_list_listbox.insert(tk.END, math137_item)

        # Creat an uneroll function
        def unenroll():
            my_math137_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_math137_label.config(text=my_math137_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_math137_label
        my_math137_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_math137_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

class Neti109Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller = controller

        # +++++++++++++++++++++++++++++
        # Header Labels for the  Header title of the Sdev220Page page
        header_label8 = tk.Label(self, text="Network Infrastructure", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

        selection_label4 = tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366',
                                    anchor='w')
        selection_label4.pack(fill='x')

        # creat a lable to design the Sdev220Page page with two colors
        button_frame = tk.Frame(self, background='#003366')
        button_frame.pack(fill='both', expand=True)

        # +++++++++++++++++++++++++++++
        # Listbox!
        # SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_neti109_list_listbox = tk.Listbox(button_frame, font=bolded, relief='raised', borderwidth=4, width=70,
                                            height=4, selectmode=tk.SINGLE)
        my_neti109_list_listbox.grid(row=0, column=2)

        # Add list of items
        my_neti109_list = ["NETI109 - Virtual - Radia Joy Perlman - M,W 2:00am-5:50am - Noblesvile - 8Wks - 3credit",
                          "NETI109 - Traditional - Dennis Moore - T,R 6:00pm-8:50pm - Lafayette - 16Wks - 3credit",
                          "NETI1109 - Learn Anywhere - Greg Ferro - M,W 4:00pm-7:50pm - Indianapolis - 8Wks - 3credit"]

        for neti109_item in my_neti109_list:
            my_neti109_list_listbox.insert(tk.END, neti109_item)

        # Creat an uneroll function
        def unenroll():
            my_neti109_label.config(text='')
            sdev220_enroll_button['state'] = tk.NORMAL
            sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat an enroll function
        def enroll():
            my_neti109_label.config(text=my_neti109_list_listbox.get(ANCHOR))
            sdev220_enroll_button['state'] = tk.DISABLED
            sdev220_unenroll_button['state'] = tk.NORMAL

        # Creat a enroll button
        sdev220_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3,
                                          width=15, height=3)
        sdev220_enroll_button.place(x=3, y=130)

        # Creat a uneroll button
        sdev220_unenroll_button = tk.Button(button_frame, text="Uneroll", relief='raised', command=unenroll,
                                            borderwidth=3, width=15, height=3, )
        sdev220_unenroll_button.place(x=179, y=130)
        sdev220_unenroll_button['state'] = tk.DISABLED

        # Creat a label to display the enrolled class
        global my_neti109_label
        my_neti109_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333',
                                    borderwidth=5, relief='raised', width=70, height=2, )
        my_neti109_label.place(x=3, y=80)

        # ++++++++++++++++++++++++++++
        # Creat a Back function
        def back():
            controller.show_frame('CoursesPage')

        # Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15,
                                 height=3)
        back_buttonn.place(x=355, y=130)
        # ++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
# ++++++++++++++++++++++++++++++
# to display everything
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
