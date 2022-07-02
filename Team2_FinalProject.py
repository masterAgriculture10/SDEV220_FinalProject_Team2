"""
SDEV 220 Team 2 Final Project
Program: Course Manager
Version: ['Python IDLE 3.10.4', 'tkinter GUI', 'Visual Studio Code',
          'GitHub.com/masterAgriculture10/SDEV220_FinalProject_Team2']
Author:  ['Yahya G. Alrobaie', 'Gunnar Dahl', 'Alvin Hampton',
          'Shanika N. Person']
Last Date
Modified: 7/2/2022
Summary:  The purpose of this program is to build a working Python system that will
          allow its users ['students', 'teachers'] to enroll in college courses.
Features: Sign in page ['UserName', 'PassWord']
          View courses
          Select course for enrollment
"""

import random
import tkinter as tk

window = tk.Tk()

for c in range(0, 15): #intial setting of 0th column and 15th rows for .grid instead of .pack
    window.columnconfigure(index=0, weight=1, minsize=75)
    window.rowconfigure(index=0, weight=1, minsize=50)
    for r in range(0):
        frame =tk.Frame(master = window, borderwidth =1)
        frame.grid(column = c, row = r)

window.title("Course Manager")

window.geometry("450x450")

canvas = tk.Canvas(window, width = "300", height = "200")
canvas.grid(columnspan = 3)

#Logo
logo = tk.PhotoImage(file = "team.png")
small = logo.subsample(1,3)
label = tk.Label(window, image = small)
label.grid(column=0, row=0)

#Defined for button command event
def sdev140():
    print("")
def sdev153():
    print("")
def sdev220():
    print("")
def cpin101():
    print("")

#Label with padding shifts all variables
title = tk.Label(text = "COURSE MANAGER START PAGE", padx = 20, pady = 20)
title.grid()

label2 = tk.Label(text = "Enter your user name")
label2.grid(column=0, row=2)

label3 = tk.Label(text = "Enter your password")
label3.grid(column=0, row=4)

#After user input information for name and bid, position button returns data
label1 = tk.Label(text = "Please select your course: ")
label1.grid(column=0, row=6)

#Entry field
entry_field1 = tk.Entry() #User Name
entry_field1.grid(column=0, row=3)

entry_field2 = tk.Entry() #Password
entry_field2.grid(column=0, row=5)

#will insert within window after button command selection, name and bid 
def getInput(): 
    name = entry_field1.get()
    bid = entry_field2.get()
    #rank = append(bid)for later maintenance
    textArea = tk.Text(master = window, height = 2, width = 30)
    textArea.grid(column=0, row=12)
    dataEntry = (name, bid)
    textArea.insert(tk.END, dataEntry)
    

#Button with padding 
button1 = tk.Button(text = "SDEV 140", command = getInput, bg = "#290001", fg = "gold")
button1.grid(column=0, row=8, padx=5, pady=5)
button1.bind("<Button-1>",sdev140)

button2 = tk.Button(text = "SDEV 153", command = getInput, bg = "#290001", fg = "gold")
button2.grid(column=0, row=9, padx=5, pady=5)
button2.bind("<Button-2>",sdev153)

button3 = tk.Button(text = "SDEV 220", command = getInput, bg = "#290001", fg = "gold")
button3.grid(column=0, row=10, padx=5, pady=5)
button3.bind("<Button-3>",sdev220)

button4 = tk.Button(text = "CPIN 101", command = getInput, bg = "#290001", fg = "gold")
button4.grid(column=0, row=11, padx=5, pady=5)
button4.bind("<Button-4>",cpin101)

window.mainloop()

