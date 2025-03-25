from tkinter import *
from tkinter import messagebox

# Dummy user data for login validation
users = {"admin": "1234"}

# Book data storage
books = []

# Function to validate login
def validate_login(username, password):
    if username in users and users[username] == password:
        return True
    return False

# Function to open the main library management window
def open_main_window():
    main_window = Toplevel()
    main_window.title("Library Management System")
    main_window.geometry("600x400")

    Label(main_window, text="Library Management System", font=("Helvetica", 16)).pack(pady=10)

    # Function to add a book
    def add_book():
        book_id = book_id_entry.get()
        book_title = book_title_entry.get()
        book_author = book_author_entry.get()
        book_count = book_count_entry.get()

        if book_id and book_title and book_author and book_count.isdigit():
            book = {
                "id": book_id,
                "title": book_title,
                "author": book_author,
                "count": int(book_count)
            }
            books.append(book)
            clear_entries()
            update_book_list()
        else:
            messagebox.showwarning("Warning", "All fields are required and count must be a number!")

    # Function to update a book
    def update_book():
        selected_book = book_listbox.curselection()
        if selected_book:
            index = selected_book[0]
            books[index] = {
                "id": book_id_entry.get(),
                "title": book_title_entry.get(),
                "author": book_author_entry.get(),
                "count": int(book_count_entry.get())
            }
            clear_entries()
            update_book_list()
        else:
            messagebox.showwarning("Warning", "No book selected!")

    # Function to delete a selected book
    def delete_book():
        selected_book = book_listbox.curselection()
        if selected_book:
            books.pop(selected_book[0])
            clear_entries()
            update_book_list()
        else:
            messagebox.showwarning("Warning", "No book selected!")

    # Function to search for books by title
    def search_book():
        search_query = search_entry.get().lower()
        filtered_books = [book for book in books if search_query in book['title'].lower()]
        update_book_list(filtered_books)

    # Function to clear the entry fields
    def clear_entries():
        book_id_entry.delete(0, END)
        book_title_entry.delete(0, END)
        book_author_entry.delete(0, END)
        book_count_entry.delete(0, END)
        search_entry.delete(0, END)

    # Function to update the listbox with current books
    def update_book_list(filtered_books=None):
        book_listbox.delete(0, END)
        for book in (filtered_books if filtered_books is not None else books):
            book_listbox.insert(END, f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Count: {book['count']}")

    # Entry fields for book details
    book_id_label = Label(main_window, text="Book ID")
    book_id_label.pack()
    book_id_entry = Entry(main_window)
    book_id_entry.pack()

    book_title_label = Label(main_window, text="Book Title")
    book_title_label.pack()
    book_title_entry = Entry(main_window)
    book_title_entry.pack()

    book_author_label = Label(main_window, text="Book Author")
    book_author_label.pack()
    book_author_entry = Entry(main_window)
    book_author_entry.pack()

    book_count_label = Label(main_window, text="Book Count")
    book_count_label.pack()
    book_count_entry = Entry(main_window)
    book_count_entry.pack()

    # Buttons for CRUD operations
    add_button = Button(main_window, text="Add Book", command=add_book)
    add_button.pack(pady=5)

    update_button = Button(main_window, text="Update Book", command=update_book)
    update_button.pack(pady=5)

    delete_button = Button(main_window, text="Delete Book", command=delete_book)
    delete_button.pack(pady=5)

    # Listbox to display books
    book_listbox = Listbox(main_window, width=80, height=10)
    book_listbox.pack(pady=10)
    
    # Entry and button for searching books
    search_label = Label(main_window, text="Search by Title")
    search_label.pack()
    search_entry = Entry(main_window)
    search_entry.pack()
    search_button = Button(main_window, text="Search", command=search_book)
    search_button.pack(pady=5)

    # Initial update of the book list
    update_book_list()

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()
    if validate_login(username, password):
        messagebox.showinfo("Login Success", "Welcome to the Library Management System!")
        login_window.destroy()
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Login Window
login_window = Tk()
login_window.title("Login")
login_window.geometry("300x200")

Label(login_window, text="Login", font=("Helvetica", 16)).pack(pady=10)

Label(login_window, text="Username").pack(pady=5)
username_entry = Entry(login_window)
username_entry.pack(pady=5)

Label(login_window, text="Password").pack(pady=5)
password_entry = Entry(login_window, show="*")
password_entry.pack(pady=5)

login_button = Button(login_window, text="Login", command=login)
login_button.pack(pady=20)

login_window.mainloop()
