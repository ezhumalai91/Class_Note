#include <iostream>
#include <string>

using namespace std;

void displayMenu();
void checkBalance(double balance);
void deposit(double &balance);
void withdraw(double &balance);
bool authenticate();

// Function to display the ATM menu
void displayMenu() {
    cout << "\nATM Menu:" << endl;
    cout << "1. Check Balance" << endl;
    cout << "2. Deposit" << endl;
    cout << "3. Withdraw" << endl;
    cout << "4. Exit" << endl;
    cout << "Enter your choice: ";
}

// Function to check the account balance
void checkBalance(double balance) {
    cout << "Your current balance is: $" << balance << endl;
}

// Function to deposit money into the account
void deposit(double &balance) {
    double amount;
    cout << "Enter amount to deposit: $";
    cin >> amount;
    if (amount > 0) {
        balance += amount;
        cout << "You have successfully deposited $" << amount << endl;
    } else {
        cout << "Invalid deposit amount. Please enter a positive amount." << endl;
    }
}

// Function to withdraw money from the account
void withdraw(double &balance) {
    double amount;
    cout << "Enter amount to withdraw: $";
    cin >> amount;
    if (amount > 0 && amount <= balance) {
        balance -= amount;
        cout << "You have successfully withdrawn $" << amount << endl;
    } else if (amount > balance) {
        cout << "Insufficient funds. Your balance is only $" << balance << endl;
    } else {
        cout << "Invalid withdrawal amount. Please enter a positive amount." << endl;
    }
}

// Function to authenticate user
bool authenticate() {
    const string correctPin = "1234"; // Predefined PIN
    string enteredPin;

        cout << "Enter your PIN: ";
        cin >> enteredPin;

        if (enteredPin == correctPin) {
            return true;
        } else {
            cout << "Incorrect PIN." << endl;
        }
    

    return false; // Authentication failed
}


int main() {
    double balance = 10000.0; // Initialize the account balance
    int choice;
    

    // Authenticate user before displaying menu
    if (!authenticate()) {
        cout << "Authentication failed. Exiting program." << endl;
        return 1;
    }

    do {
        displayMenu(); // Show the menu
        cin >> choice; // Get user choice

        switch (choice) {
            case 1:
                checkBalance(balance);
                break;
            case 2:
                deposit(balance);
                break;
            case 3:
                withdraw(balance);
                break;
            case 4:
                cout << "Exiting... Thank you for using the ATM." << endl;
                break;
            default:
                cout << "Invalid choice. Please enter a number between 1 and 4." << endl;
                break;
        }
    } while (choice != 4); // Continue until user chooses to exit

    return 0;
}