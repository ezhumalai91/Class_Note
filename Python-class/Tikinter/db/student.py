import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="StudentDB"
    )

# Function to register a student
def register_student():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    course = entry_course.get()

    if first_name and last_name and email and phone and course:
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Students (first_name, last_name, email, phone, course) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, last_name, email, phone, course)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Student registered successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields")

# Function to clear entry fields
def clear_entries():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_course.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Student Registration")

# Create and place labels and entry fields
tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=10)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=10)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Phone").grid(row=3, column=0, padx=10, pady=10)
entry_phone = tk.Entry(root)
entry_phone.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Course").grid(row=4, column=0, padx=10, pady=10)
entry_course = tk.Entry(root)
entry_course.grid(row=4, column=1, padx=10, pady=10)

# Create and place the register button
register_button = tk.Button(root, text="Register", command=register_student)
register_button.grid(row=5, column=0, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
