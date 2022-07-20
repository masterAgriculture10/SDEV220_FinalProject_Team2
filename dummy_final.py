from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

window = Tk()
# window.geometry('800x800')
notebook = ttk.Notebook(window)

tab1 = Frame(notebook, width=800, height=800)
tab2 = Frame(notebook, width=800, height=800, bg='#bcd9ba')

notebook.add(tab1, text='COURSES')
notebook.add(tab2, text='SCHEDULE')
notebook.pack(expand=True,fill='both')

def enroll():
    myLabel = Label(tab2, text=addClass.get()).pack()

def desc(event):
    if addClass.get() == 'Accounting (ACCT)':
        myLabel =Label(tab1, text='Introduces the fundamental principles, techniques, and tools of financial accounting. The development and use of the basic financial statements pertaining to corporations both service and retail')
        myLabel.place(relx=.6, rely=.6)
    if addClass.get() == 'Biology (BIOL)':
        myLabel=Label(tab1, text='Introduces the basic concepts of life. Includes discussion of cellular and organismal biology, genetics, evolution, ecology, and interaction among all living organisms. Addresses applications of biology in a global community')
        myLabel.pack(side=RIGHT)


#
# def comboclick(event):
#     myLabel = Label(tab1, text=myCombo.get()).pack()


options = [
    'Accounting (ACCT)',
    'Biology (BIOL)',
    'Computer Science (CSCI)',
    'Design Technology (DESN)',
    'Engineering (ENGR)',
    'Heating & Cooling (HVAC)',
    'Legal Studies (LEGS)',
    'Mathematics (MATH)',
    'Network Infrastructure (NETI)',
    'Psychology (PSYC)',
    'Software Development (SDEV)',
    'Visual Communication (VISC)'
]



addClass = StringVar()
addClass.set('SELECT COURSE')

classes = OptionMenu(tab1, addClass, *options, command=desc)
classes.place(relx=.1, rely=.2)

# myCombo = ttk.Combobox(tab1, value=options)
# myCombo.current()
# myCombo.bind('<<ComboboxSelected>>', comboclick)
# myCombo.pack()

Enroll = Button(tab1, text='Enroll', command=enroll, height=4, width=30, bg='#3f703d').place(relx=.5,rely=.8)




window.mainloop()








#
# options = {
#     'Accounting (ACCT)' : 'Introduces the fundamental principles, techniques, and tools of financial accounting. The development and use of the basic financial statements pertaining to corporations both service and retail',
#     'Biology (BIOL)' : 'Introduces the basic concepts of life. Includes discussion of cellular and organismal biology, genetics, evolution, ecology, and interaction among all living organisms. Addresses applications of biology in a global community',
#     'Computer Science (CSCI)' : 'Introduces the fundamental concepts of procedural programming. Topics include data types, control structures, functions, arrays, files, and the mechanics of running, testing, and debugging.',
#     'Design Technology (DESN)' : 'The purpose of this introductory course is to provide students with a basic understanding of sketching practices and the features and considerations associated with the operation of computer-aided design (CAD) systems. Students will gain valuable hands-on experience creating sketches and using CAD software.',
#     'Engineering (ENGR)' : ' Provides an introduction to the engineering profession and to campus resources. The course is designed to help students develop essential communication and thinking skills along with the study and time-management skills needed for success in studying engineering.',
#     'Heating & Cooling (HVAC)' : 'This course covers many of the topics needed for students to be successful in the mechanical construction industry. Its modules include: history of the HVAC industry, OSHA 10-hour construction industry training, communication and customer service skills, and an introduction to blueprints and other types of mechanical drawings.',
#     'Legal Studies (LEGS)' : 'Introduction to Legal Studies will provide the student a broad understanding of the American legal system. Students will engage with and learn about the various court structures, the key players within the system and how our laws and rules are made, enforced, interpreted, and applied.',
#     'Mathematics (MATH)' : 'Presents an in-depth study of functions, quadratic, polynomial, radical, and rational equations, radicals, complex numbers, absolute value equations and inequalities, rational fractions and exponential and logarithmic functions.',
#     'Network Infrastructure (NETI)' : 'The course is intended to provide students with an understanding of fundamental concepts in networking. All layers of the OSI and TCP/IP Models are examined to illustrate concepts and to provide insight into data communications, networking, and the Internet.',
#     'Psychology (PSYC)' : 'Surveys behavior and cognitive processes as they affect the individual. The course focuses on biological foundations, learning processes, research methodologies, personality, human development and abnormal and social psychology.',
#     'Software Development (SDEV)' : 'Introduces students to concepts and practices of programming languages and software development. Students are introduced to algorithms and development tools used to document/implement computer logic.',
#     'Visual Communication (VISC)' : 'This course introduces students to fundamental design theory.  Investigations into design theory and color dynamics will provide experiences in applying design theory, ideas and creative problem solving, critical peer evaluation, and presentation skills.'
# }