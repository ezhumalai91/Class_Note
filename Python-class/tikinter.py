
'''
from tkinter import *
  
root = Tk() 
a = Label(root, text ="Hello World") 
a.pack() 
  
root.mainloop()
'''


from tkinter import *

# Create the main window
base = Tk()
base.geometry('500x500')
base.title("Registration Form")

# Title label
labl_0 = Label(base, text="Registration Form", width=20, font=("bold", 20))
labl_0.place(x=90, y=53)

# Full Name label and entry
labl_1 = Label(base, text="Full Name", width=20, font=("bold", 10))
labl_1.place(x=80, y=130)

entry_1 = Entry(base)
entry_1.place(x=240, y=130)

# Email label and entry
labl_2 = Label(base, text="Email", width=20, font=("bold", 10))
labl_2.place(x=68, y=180)

entry_02 = Entry(base)
entry_02.place(x=240, y=180)

# Gender label and radio buttons
labl_3 = Label(base, text="Gender", width=20, font=("bold", 10))
labl_3.place(x=70, y=230)

var = IntVar()
Radiobutton(base, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(base, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

# Age label and entry
labl_4 = Label(base, text="Age", width=20, font=("bold", 10))
labl_4.place(x=70, y=280)

entry_03 = Entry(base)
entry_03.place(x=240, y=280)

# Submit button
Button(base, text='Submit', width=20, bg='brown', fg='white').place(x=180, y=380)

# Run the main loop
base.mainloop()

