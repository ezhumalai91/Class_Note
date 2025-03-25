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

# Create StringVar objects to store input and result
num1_var = tk.StringVar()
num2_var = tk.StringVar()
result_var = tk.StringVar()

# Update the result when the input changes
num1_var.trace("w", update_result)
num2_var.trace("w", update_result)

# Create and place the input boxes and result label
tk.Label(root, text="Input 1:").grid(row=0, column=0)
entry1 = tk.Entry(root, textvariable=num1_var)
entry1.grid(row=0, column=1)

tk.Label(root, text="Input 2:").grid(row=1, column=0)
entry2 = tk.Entry(root, textvariable=num2_var)
entry2.grid(row=1, column=1)

tk.Label(root, text="Result:").grid(row=2, column=0)
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=2, column=1)

# Start the main event loop
root.mainloop()
