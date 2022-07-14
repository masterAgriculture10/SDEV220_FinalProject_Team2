"""
Tkinter GUI stuff
"""

import tkinter as tk


database = {"yahya": "1111", "gunnar": "2222", "alvin": "3333", "shanika": "4444"}
print(f'account details: {database}')


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

#the container is where we'll stackabunch of frames
#on top of each other, then the one we want visible
#will be raised above the others
        self.shared_data = {'Balance':tk.IntVar()}
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, CoursesPage, Sdev153Page, Sdev140Page, Sdev220Page,):
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
        
        self.controller.title('ATM')
# options for the screen size normal, iconic, withdrawn, or zoomed
        self.controller.state('normal')

# Creat a function to clear the entries Widget conten
        def clear_text():
            user_entry_Box.delete(0, tk.END)
            pin_entry_Box.delete(0, tk.END)


#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the login page
        header_label1 = tk.Label(self, text="IVY ATM", foreground='White', background='#336699', font=('bold', 50))
        header_label1.pack()

        header_label2 = tk.Label(self, text="Login to Your Account", foreground='White', background='#336699', font=('bold', 50))
        header_label2.pack(pady=30)
# Creat a space lable 
        space_label = tk.Label(self, height=5, background='#003366')
        space_label.pack()

# ++++++++++++++++++++++++++++
# Creat a pin Label to ask the user to enter the pin
        user_label = tk.Label(self, text='Enter your Username:', font=15, background='#003366')
        user_label.place(x=8,y=180)


# Creat a entery box, to put the pin
        user = tk.StringVar()      
        user_entry_Box = tk.Entry(self, textvariable=user)
        user_entry_Box.focus_set()
        user_entry_Box.place(x=170, y=180)


#++++++++++++++++++++++++++++ #336699
# Creat a pin Label to ask the user to enter the pin 
        pin_label = tk.Label(self, text='Enter your PIN number:', font=15, background='#003366')
        pin_label.place(x=8,y=210) 

# Creat a entery box, to put the pin
        pin = tk.StringVar()      
        pin_entry_Box = tk.Entry(self, textvariable=pin)
        pin_entry_Box.place(x=170,y=210)

# Creat a login function to check the user validate the user login

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
        enter_button = tk.Button(self, text='Enter', command=login_check, relief='flat', width=10, )
        enter_button.place(x=10, y=250)

# creat a Exit Button to quit the program
        button_quit = tk.Button(self, text="Exit", command=self.quit,relief='flat', width=10,)
        button_quit.place(x=180, y=250)
# creat a Clear Button to Clear the login text
        button_clear = tk.Button(self, text="Clear", command=clear_text,relief='flat', width=10,)
        button_clear.place(x=350, y=250)


# Creat a display message when the user enter the incorrect login 
        incorrect_login_label = tk.Label(self, text="", background='#336699', foreground='#990033', font=('bold', 22), anchor='n')
        incorrect_login_label.pack(fill='both', expand=True)

#+++++++++++++++++++++++++++++++++
# Creat a Bottom frame to display the time and the user pin.
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

#++++++++++++++++++++++++++++++++
    ##    card_photo = tk.PhotoImage(file='creditcard1.png')
     # #  card_label = tk.Label(bottom_frame,image=card_photo)
      ##  card_label.pack(side='left')
      ##  card_label.image = card_photo

#+++++++++++++++++++++++
# Creat class to the second window( TransactionPage: Deposit, Withdraw, Balance,Exit)
class CoursesPage(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, background='#660066')
            self.controller=controller

 #+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the TransactionPage page
            header_label3 = tk.Label(self, text="IVY SDVE Courses", foreground='White', background='#660066', font=('bold', 50))
            header_label3.pack()

# Header Labels for the  Header title of the TransactionPage page
            header_label4 = tk.Label(self, text="Courses", foreground='White', background='#660066', font=('bold', 25))
            header_label4.pack(pady=5)

            selection_label= tk.Label(self, text="Select a course to enroll", fg='white', background='#003366' ,anchor='w')
            selection_label.pack(fill='x')

# Creat a frame to display the transaction button.
            button_frame = tk.Frame(self, background='#003366')
            button_frame.pack(fill='both', expand=True)

# ++++++++++++++++++++++++++++
# Creat a Withdraw function
            def sdev_153():
                controller.show_frame('Sdev153Page')
# Creat a withdraw button
            withdraw_button = tk.Button(button_frame, text="SDEV153", command=sdev_153, relief='raised', borderwidth=3, width=25, height=5)
            withdraw_button.grid(row=0, column=0)

# ++++++++++++++++++++++++++++
# Creat a deposit function
            def sdev_140():
                controller.show_frame('Sdev140Page')
# Creat a deposit button
            deposit_button = tk.Button(button_frame, text="SDEV140", command=sdev_140, relief='raised', borderwidth=3, width=25, height=5)
            deposit_button.grid(row=1, column=0)

# ++++++++++++++++++++++++++++
# Creat a balance function
            def sdev_220():
                controller.show_frame('Sdev220Page')
# Creat a balance button
            balance_button = tk.Button(button_frame, text="SDEV220", command=sdev_220, relief='raised', borderwidth=3, width=25, height=5)
            balance_button.grid(row=0, column=1)

# ++++++++++++++++++++++++++++
# Creat a exit function
            def exit():
                controller.show_frame('StartPage')
# Creat a exit button
            exit_button = tk.Button(button_frame, text="LogOut", command=exit, relief='raised', borderwidth=3,width=25, height=5)
            exit_button.grid(row=1,column=1,)

#+++++++++++++++++++++++++++++++++
# Creat a Bottom frame to display the time.
            bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
            bottom_frame.pack(fill='x',side='bottom')


#+++++++++++++++++++++++++++++
# Creat class to the WithdrawPage window( TransactionPage: Deposit, Withdraw, Balance,Exit)

class Sdev153Page (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the WithdrawPage page
        header_label5 = tk.Label(self, text="Schedules", foreground='White', background='#660066', font=('bold', 50))
        header_label5.pack()

        button_frame = tk.Frame(self, background='#336699' )
        button_frame.pack(fill='both', expand=True)

# Creat a Bottom to display the Sdev153 schedules options.

        twenty_button = tk.Button(button_frame, text='20', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        twenty_button.grid(row=0,column=0)

        forty_button = tk.Button(button_frame, text='40', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        forty_button.grid(row=1,column=0) 

        sixty_button = tk.Button(button_frame, text='60', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        sixty_button.grid(row=2,column=0) 

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', width=10)
        back_buttonn.grid(row=4,column=0, columnspan=2)
#++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')


#++++++++++++++++++++++++++
# Creat class to the DepositPage window( TransactionPage: Deposit, Withdraw, Balance,Exit)

class Sdev140Page (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the DepositPage page
        header_label7 = tk.Label(self, text="Schedules", foreground='White', background='#660066', font=('bold', 50))
        header_label7.pack()

        button_frame = tk.Frame(self, background='#336699' )
        button_frame.pack(fill='both', expand=True)


# Creat a Bottom to display the Sdev153 schedules options.

        twentyy_button = tk.Button(button_frame, text='20', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        twentyy_button.grid(row=0,column=0)

        fortyy_button = tk.Button(button_frame, text='40', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        fortyy_button.grid(row=1,column=0) 

        sixtyy_button = tk.Button(button_frame, text='60', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        sixtyy_button.grid(row=2,column=0) 

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', width=10)
        back_buttonn.grid(row=4,column=0, columnspan=2)
#++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')


# Creat class to the class BalancePage window( TransactionPage: Deposit, Withdraw, Balance,Exit)
class Sdev220Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller=controller

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the BalancePage page
        header_label8 = tk.Label(self, text="Schedules", foreground='White', background='#660066', font=('bold', 50))
        header_label8.pack()

# creat a lable to design the deposit page with two colores
        button_frame = tk.Frame(self, background='#336699')
        button_frame.pack(fill='both', expand=True)

# Creat a Bottom to display the Sdev153 schedules options.

        twentyyy_button = tk.Button(button_frame, text='20', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        twentyyy_button.grid(row=0,column=0)

        fortyyy_button = tk.Button(button_frame, text='40', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        fortyyy_button.grid(row=1,column=0) 

        sixtyyy_button = tk.Button(button_frame, text='60', command=exit, relief='raised', borderwidth=4,width=54, height=3)
        sixtyyy_button.grid(row=2,column=0) 

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', width=10)
        back_buttonn.grid(row=4,column=0, columnspan=2)
#++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
