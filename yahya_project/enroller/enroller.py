"""
ATM
05/16/2022
version 3.0
1.This program will do what the ATM  does, it will verify the user validity through the username and password. 
2.Give the user several options, which are 1.Deposit 2.Withdrawal 3.Balance Inquiry  4.Log Out.
Ckeck if  they try to withdraw more money than there is, a warning will be given to the customer. 
username is :yahya 
pin is:   0000
"""


from cgitb import text
import tkinter as tk
from PIL import ImageTk, Image
import time


#my_img = ImageTk.PhotoImage(Image.open("smokey.gif"))
#my_lable = Label(image=my_img)
#my_lable.pack

balance = 1000

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
        for F in (StartPage, TransactionPage, WithdrawPage, DepositPage, BalancePage,):
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

        #my_img = ImageTk.PhotoImage(Image.open("atm.png"))
        #my_lable = Label(image=my_img)
        #my_lable.pack()

   
        self.controller.iconphoto(False, ImageTk.PhotoImage(file='/Users/yahyaalrobaie/Documents/Python IDE/Final_ATM2/atm.png'))
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
            if pin.get() == '0000' and user.get() == 'yahya':
               pin.set('')  
               user.set('')
               incorrect_login_label['text']=''
               controller.show_frame('TransactionPage')
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
        card_photo = tk.PhotoImage(file='creditcard1.png')
        card_label = tk.Label(bottom_frame,image=card_photo)
        card_label.pack(side='left')
        card_label.image = card_photo

#+++++++++++++++++++++++++++++++++
# Creat a time function to display the current time.
        def timee():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,timee)
            
        time_label = tk.Label(bottom_frame,font=(12))
        time_label.pack(side='right')

        timee()

#+++++++++++++++++++++++
# Creat class to the second window( TransactionPage: Deposit, Withdraw, Balance,Exit)
class TransactionPage(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, background='#003366')
            self.controller=controller


 #+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the TransactionPage page
            header_label3 = tk.Label(self, text="IVY ATM", foreground='White', background='#336699', font=('bold', 50))
            header_label3.pack()

# Header Labels for the  Header title of the TransactionPage page
            header_label4 = tk.Label(self, text="Transactions", foreground='White', background='#003366', font=('bold', 25))
            header_label4.pack(pady=5)

            selection_label= tk.Label(self, text="Select transaction type", fg='white', background='#003366' ,anchor='w')
            selection_label.pack(fill='x')

# Creat a frame to display the transaction button.
            button_frame = tk.Frame(self, background='#336699')
            button_frame.pack(fill='both', expand=True)

# ++++++++++++++++++++++++++++
# Creat a Withdraw function
            def withdraw():
                controller.show_frame('WithdrawPage')

# Creat a withdraw button
            withdraw_button = tk.Button(button_frame, text="Withdraw", command=withdraw, relief='raised', borderwidth=3, width=25, height=5)
            withdraw_button.grid(row=0, column=0)

# ++++++++++++++++++++++++++++
# Creat a deposit function
            def deposit():
                controller.show_frame('DepositPage')

# Creat a deposit button
            deposit_button = tk.Button(button_frame, text="Deposit", command=deposit, relief='raised', borderwidth=3, width=25, height=5)
            deposit_button.grid(row=1, column=0)

# ++++++++++++++++++++++++++++
# Creat a balance function
            def balance():
                controller.show_frame('BalancePage')

# Creat a balance button
            balance_button = tk.Button(button_frame, text="Balance", command=balance, relief='raised', borderwidth=3, width=25, height=5)
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

# Creat a time function to display the current time.
            def timee():
                current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
                time_label.config(text=current_time)
                time_label.after(200,timee)
                
            time_label = tk.Label(bottom_frame,font=(12))
            time_label.pack(side='right')

            timee()

#+++++++++++++++++++++++++++++
# Creat class to the WithdrawPage window( TransactionPage: Deposit, Withdraw, Balance,Exit)

class WithdrawPage (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#003366')
        self.controller=controller
#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the WithdrawPage page
        header_label5 = tk.Label(self, text="IVY ATM", foreground='White', background='#336699', font=('bold', 50))
        header_label5.pack()

# Header Labels for the  Header title of the WithdrawPage page
        header_label6 = tk.Label(self, text="Choose the amount you want to withdraw", foreground='White', background='#003366', font=('bold', 15))
        header_label6.pack(pady=5)

        button_frame = tk.Frame(self, background='#336699' )
        button_frame.pack(fill='both', expand=True)

# Creat a withdraw for the amount options(20, 40,60,80,100, other)
        def withdraw(amount):
                global balance
                if amount <= balance:
                    balance = balance - amount
                    incorrect_withdraw_label['text']=''
                    controller.shared_data['Balance'].set(balance)
                    controller.show_frame('TransactionPage')
                else:
                     incorrect_withdraw_label['text']='Insufficient amount'
       
# Creat a display message when the user enter the incorrect login 
        incorrect_withdraw_label = tk.Label(self, text="", background='#336699', foreground='#990033', font=('bold', 22), anchor='n')
        incorrect_withdraw_label.pack(fill='both', expand=True)


        twenty_button = tk.Button(button_frame, text='20', command=lambda:withdraw(20), relief='raised', borderwidth=3,width=25, height=3)
        twenty_button.grid(row=0,column=0)

        forty_button = tk.Button(button_frame, text='40', command=lambda:withdraw(40), relief='raised', borderwidth=3,width=25, height=3)
        forty_button.grid(row=1,column=0) 

        sixty_button = tk.Button(button_frame, text='60', command=lambda:withdraw(60), relief='raised', borderwidth=3,width=25, height=3)
        sixty_button.grid(row=2,column=0) 

        eighty_button = tk.Button(button_frame, text='80', command=lambda:withdraw(80), relief='raised', borderwidth=3,width=25, height=3)
        eighty_button.grid(row=0,column=1) 

        one_hundred_button = tk.Button(button_frame, text='100', command=lambda:withdraw(100), relief='raised', borderwidth=3,width=25, height=3)
        one_hundred_button.grid(row=1,column=1)

        two_hundred_button = tk.Button(button_frame, text='200', command=lambda:withdraw(200), relief='raised', borderwidth=3,width=25, height=3)
        two_hundred_button.grid(row=2,column=1)

# Creat a variable to hold the other amount  
        cash = tk.StringVar()
        other_amount_entry= tk.Entry(button_frame, textvariable=cash, width=20)
        other_amount_entry.grid(row=3, column=0, columnspan=2, pady=5)

        def other_amount(_):
            global balance
            balance -=int(cash.get())
            controller.shared_data['Balance'].set(balance)
            cash.set('')
            controller.show_frame('TransactionPage')
            other_amount_entry.bind('<return>', other_amount)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('TransactionPage')

# Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', width=10)
        back_buttonn.grid(row=4,column=0, columnspan=2)

#++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')


# Creat a time function to display the current time.
        def timee():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,timee)
            
        time_label = tk.Label(bottom_frame,font=(12))
        time_label.pack(side='right')

        timee()

#++++++++++++++++++++++++++
# Creat class to the DepositPage window( TransactionPage: Deposit, Withdraw, Balance,Exit)

class DepositPage (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#003366')
        self.controller=controller

#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the DepositPage page
        header_label7 = tk.Label(self, text="IVY ATM", foreground='White', background='#336699', font=('bold', 50))
        header_label7.pack()

# Creat a space lable 
        space_label = tk.Label(self, height=5, background='#003366')
        space_label.pack(pady=20)

# ++++++++++++++++++++++++++++
# Creat a pin Label to ask the user to enter the pin
        enter_amount_label = tk.Label(self, text='Enter amount:', font=15, background='#003366')
        enter_amount_label.pack(pady=10)
#
        cash = tk.StringVar()
        deposit_entry = tk.Entry(self, text=cash )
        deposit_entry.pack()

# Creat a deposit cash function to add the amount to the balance
        def deposit_cash():
            global balance
            balance += int(cash.get())
            controller.shared_data['Balance'].set(balance)
            controller.show_frame('TransactionPage')
            cash.set('')

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('TransactionPage')

# creat a button to enter the deposit amount
        enter_deposit_amount = tk.Button(self,text='Enter', command=deposit_cash, relief='raised', borderwidth=3, width=15, height=2)
        enter_deposit_amount.pack(pady=10)


# Creat a Back button
        back_buttonn = tk.Button(self, text="Back", command=back, relief='raised', borderwidth=3, width=15, height=2)
        back_buttonn.pack()

# creat a lable to design the deposit page with two colores

        two_tone_lable = tk.Label(self, background='#336699')
        two_tone_lable.pack(fill='both', expand=True)




# Creat class to the class BalancePage window( TransactionPage: Deposit, Withdraw, Balance,Exit)

class BalancePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#003366')
        self.controller=controller


#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the BalancePage page
        header_label8 = tk.Label(self, text="IVY ATM", foreground='White', background='#336699', font=('bold', 50))
        header_label8.pack()

# global balance to display the balance  in the balance label
        global balance  
        controller.shared_data['Balance'].set(balance)

        balance_label = tk.Label(self,textvariable=controller.shared_data['Balance'], font=('bold', 20), background='#336699',)
        balance_label.pack(fill='x', pady=10)

# creat a lable to design the deposit page with two colores
        button_frame = tk.Frame(self, background='#336699')
        button_frame.pack(fill='both', expand=True)

#+++++++++++++++++++++++++++++++++
# Creat a menu function to get back to the TransactionPage 
        def menu():
            controller.show_frame('TransactionPage')

# Creat a button for the menu
        menu_buttone = tk.Button(button_frame,text='Menu', command=menu, relief='raised', borderwidth=5, width=50, height=3)
        menu_buttone.grid(row=0, column=0, pady=5, padx=10)

# Creat a menu function to get back to the LoginPage 
        def exit():
            controller.show_frame('StartPage')

# Creat a button for the exit
        exit_button = tk.Button(button_frame,text='LogOut',command=exit,relief='raised',borderwidth=5,width=50,height=3)
        exit_button.grid(row=1,column=0,pady=5)


#++++++++++++++++++++++++++++++
# to display everything
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()