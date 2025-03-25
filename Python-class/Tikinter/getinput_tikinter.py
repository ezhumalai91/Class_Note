from tkinter import *
import tkinter as tk
m = tk.Tk()
m.title("Welcome App")

def hai():
    # Get the user's input from the entry widget
    user_input = entry.get()
    welcome_message = f"WELCOME, {user_input}!"
    welcome_label = tk.Label(m, text=welcome_message, fg="red")
    welcome_label.pack()
entry = tk.Entry(m, width=30)
entry.pack()
b1 = tk.Button(m, text="CLICK HERE", command=hai, bg="gray", fg="yellow")
b1.pack()
m.mainloop()
