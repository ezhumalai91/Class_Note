import tkinter as tk

def update_result(*args):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_var.set(num1 + num2)
    except ValueError:
        result_var.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Auto Sum Calculator")

# Set the size of the window
root.geometry('300x200')

# Center the window on the screen
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Create StringVar objects to store input and result
num1_var = tk.StringVar()
num2_var = tk.StringVar()
result_var = tk.StringVar()

# Update the result when the input changes
num1_var.trace("w", update_result)
num2_var.trace("w", update_result)

# Define a larger font
font = ('Helvetica', 14)

# Create and place the input boxes and result label
tk.Label(root, text="Input 1:", font=font).grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root, textvariable=num1_var, font=font)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Input 2:", font=font).grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root, textvariable=num2_var, font=font)
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Result:", font=font).grid(row=2, column=0, padx=10, pady=10)
result_label = tk.Label(root, textvariable=result_var, font=font)
result_label.grid(row=2, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
