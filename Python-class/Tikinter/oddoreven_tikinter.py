from tkinter import *
import tkinter as tk

# Create the main window
m = tk.Tk()
m.title("Odd or Even Checker")

def check_odd_even():
    # Get the user's input from the entry widget
    user_input = entry.get()
    
    # Check if the input is a valid integer
    try:
        number = int(user_input)
        if number % 2 == 0:
            result = "Even"
        else:
            result = "Odd"
        result_label.config(text=f"The number {number} is {result}.", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid integer!", fg="red")

# Create an entry widget to get user input
entry = tk.Entry(m, width=30)
entry.pack()

# Create the button to check odd or even
check_button = tk.Button(m, text="Check", command=check_odd_even)
check_button.pack()

# Label to display the result
result_label = tk.Label(m, text="", fg="green")
result_label.pack()

# Start the main loop
m.mainloop()
