
'''
# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == "hello"):
		txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

	elif (user == "how are you"):
		txt.insert(END, "\n" + "Bot -> fine! and you")

	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Bot -> My pleasure !")

	elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
		txt.insert(END, "\n" + "Bot -> We have coffee and tea")

	elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
		txt.insert(
			END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

	elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
		txt.insert(END, "\n" + "Bot -> Have a nice day!")
	elif "name" in user:
		txt.insert(END, "\n" + "My name is chatbot")
	else:
		txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

	e.delete(0, END)
'''

from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def send():
    # Get user input from the entry widget and format it
    user_input = e.get()
    send = "You -> " + user_input
    txt.insert(END, "\n" + send)

    # Convert user input to lowercase for case-insensitive matching
    user = user_input.lower()

    # Define a dictionary with predefined responses
    responses = {
        "name":"My name is chatbot",
        "hello": "Hi there, how can I help?",
        "hi": "Hi there, what can I do for you?",
        "hii": "Hi there, what can I do for you?",
        "hiiii": "Hi there, what can I do for you?",
        "how are you": "Fine! And you?",
        "fine": "Great! How can I help you?",
        "i am good": "Great! How can I help you?",
        "i am doing good": "Great! How can I help you?",
        "thanks": "My pleasure!",
        "thank you": "My pleasure!",
        "now it's my time": "My pleasure!",
        "what do you sell": "We have coffee and tea.",
        "what kinds of items are there": "We have coffee and tea.",
        "have you something": "We have coffee and tea.",
        "tell me a joke": "What did the buffalo say when his son left for college? Bison!",
        "tell me something funny": "What did the buffalo say when his son left for college? Bison!",
        "crack a funny line": "What did the buffalo say when his son left for college? Bison!",
        "goodbye": "Have a nice day!",
        "see you later": "Have a nice day!",
        "see yaa": "Have a nice day!"
    }

    # Use the get method to find the response, default to a message if not found
    response = responses.get(user, "Sorry! I didn't understand that.")

    # Special case handling for "name" in user input
    if "name" in user:
        response = "My name is chatbot."

    # Insert the bot's response into the text widget
    txt.insert(END, "\nBot -> " + response)

    # Clear the entry widget for the next input
    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
