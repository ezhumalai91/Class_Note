from tkinter import *
import calendar

# Function for showing the calendar of the given month and year
def showCal() :
    # Create a GUI window
    new_gui = Tk()
    
    # Set the background colour of GUI window
    new_gui.config(background = "white")

    # Set the name of tkinter GUI window 
    new_gui.title("CALENDAR")

    # Set the configuration of GUI window
    new_gui.geometry("300x250")

    # Get the year and month from the text entries
    fetch_year = int(year_field.get())
    fetch_month = int(month_field.get())

    # Use monthcalendar method to get the calendar for the specified month and year
    cal_content = calendar.month(fetch_year, fetch_month)

    # Create a label for showing the content of the calendar
    cal_month = Label(new_gui, text = cal_content, font = "Consolas 10 bold")

    # Grid method is used for placing the widgets at respective positions in table-like structure
    cal_month.grid(row = 5, column = 1, padx = 20)
    
    # Start the GUI 
    new_gui.mainloop()

# Driver Code
if __name__ == "__main__" :
    # Create a GUI window
    gui = Tk()
    
    # Set the background colour of GUI window
    gui.config(background = "white")

    # Set the name of tkinter GUI window 
    gui.title("CALENDAR")

    # Set the configuration of GUI window
    gui.geometry("250x180")

    # Create a CALENDAR : label with specified font and size
    cal = Label(gui, text = "CALENDAR", bg = "dark gray",
                            font = ("times", 28, 'bold'))

    # Create Enter Year and Enter Month labels
    year = Label(gui, text = "Enter Year", bg = "light green")
    month = Label(gui, text = "Enter Month", bg = "light green")
    
    # Create text entry boxes for filling or typing the information
    year_field = Entry(gui)
    month_field = Entry(gui)

    # Create a Show Calendar Button and attach it to showCal function
    Show = Button(gui, text = "Show Calendar", fg = "Black",
                            bg = "Red", command = showCal)

    # Create an Exit Button and attach it to exit function
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
    
    # Grid method is used for placing the widgets at respective positions in table-like structure
    cal.grid(row = 1, column = 1)

    year.grid(row = 2, column = 1)
    year_field.grid(row = 3, column = 1)

    month.grid(row = 4, column = 1)
    month_field.grid(row = 5, column = 1)

    Show.grid(row = 6, column = 1)
    Exit.grid(row = 7, column = 1)
    
    # Start the GUI 
    gui.mainloop()
