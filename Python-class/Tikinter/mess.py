from tkinter import *
import tkinter

m = tkinter.Tk()

def hai():
    # Create a label with the welcome message
    welcome_label = Label(m, text="WELCOME", fg="red",bg="green")
    # Place the label below the button
    welcome_label.pack()

# Create the button
b1 = Button(m, text="CLICK HERE", command=hai, bg="gray", fg="yellow")
b1.pack()

# Start the main loop
mainloop()
