from tkinter import *
from tkinter import simpledialog, messagebox

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")

        self.balance = 100000  # Initial balance

        # Create GUI elements
        self.label_balance = Label(master, text="Balance: $100000")
        self.label_balance.pack()

        self.button_deposit = Button(master, text="Deposit", command=self.deposit)
        self.button_deposit.pack()

        self.button_withdraw = Button(master, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack()

    def deposit(self):
        deposit_amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:", parent=self.master)
        if deposit_amount:
            self.balance += deposit_amount
            self.update_balance()

    def withdraw(self):
        withdraw_amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:", parent=self.master)
        if withdraw_amount and withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            self.update_balance()
        else:
            messagebox.showerror("Error", "Insufficient funds")

    def update_balance(self):
        self.label_balance.config(text="Balance: ${}".format(self.balance))


def main():
    root = Tk()
    atm = ATM(root)
    root.mainloop()

if __name__ == "__main__":
    main()
