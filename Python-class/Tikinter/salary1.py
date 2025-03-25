import tkinter as tk

def calculate_allowances(*args):
    try:
        salary = float(salary_var.get())
        hra = salary * 0.20  # Example: 20% of salary
        ca = salary * 0.10   # Example: 10% of salary
        tds = salary * 0.15  # Example: 15% of salary
        
        hra_var.set(f"{hra:.2f}")
        ca_var.set(f"{ca:.2f}")
        tds_var.set(f"{tds:.2f}")
    except ValueError:
        hra_var.set("Invalid input")
        ca_var.set("Invalid input")
        tds_var.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Salary Allowances Calculator")

# Create StringVar objects to store input and results
salary_var = tk.StringVar()
hra_var = tk.StringVar()
ca_var = tk.StringVar()
tds_var = tk.StringVar()

# Update the allowances when the salary input changes
salary_var.trace("w", calculate_allowances)

# Create and place the input box and result text boxes
tk.Label(root, text="Salary:").grid(row=0, column=0)
salary_entry = tk.Entry(root, textvariable=salary_var)
salary_entry.grid(row=0, column=1)

tk.Label(root, text="HRA:").grid(row=1, column=0)
hra_entry = tk.Entry(root, textvariable=hra_var, state='readonly')
hra_entry.grid(row=1, column=1)

tk.Label(root, text="CA:").grid(row=2, column=0)
ca_entry = tk.Entry(root, textvariable=ca_var, state='readonly')
ca_entry.grid(row=2, column=1)

tk.Label(root, text="TDS:").grid(row=3, column=0)
tds_entry = tk.Entry(root, textvariable=tds_var, state='readonly')
tds_entry.grid(row=3, column=1)

# Start the main event loop
root.mainloop()
