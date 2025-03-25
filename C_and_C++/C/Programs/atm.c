#include <stdio.h>

int main() {
    int pin = 1234, enteredPin, option, amount, balance = 100000;
    int isPinCorrect = 0;

    printf("Welcome to the ATM\n");

    // Loop to validate the PIN
    for (int attempts = 3; attempts > 0; attempts--) {
        printf("Please enter your PIN: ");
        scanf("%d", &enteredPin);

        if (enteredPin == pin) {
            isPinCorrect = 1;
            break;
        } else {
            printf("Incorrect PIN. You have %d attempt(s) left.\n", attempts - 1);
        }
    }

    // If the PIN is correct, display the options
    if (isPinCorrect) {
        printf("Login successful!\n");

        // Main menu loop
        while(1) {
            printf("\nATM Menu:\n");
            printf("1. Check Balance\n");
            printf("2. Withdraw Cash\n");
            printf("3. Deposit Cash\n");
            printf("4. Exit\n");
            printf("Please choose an option: ");
            scanf("%d", &option);

            if (option == 1) {
                // Check balance
                printf("Your balance is: $%d\n", balance);
            } else if (option == 2) {
                // Withdraw cash
                printf("Enter amount to withdraw: ");
                scanf("%d", &amount);

                if (amount <= balance) {
                    balance -= amount;
                    printf("Please collect your cash. Your new balance is: $%d\n", balance);
                } else {
                    printf("Insufficient balance.\n");
                }
            } else if (option == 3) {
                // Deposit cash
                printf("Enter amount to deposit: ");
                scanf("%d", &amount);
                balance += amount;
                printf("Amount deposited. Your new balance is: $%d\n", balance);
            } else if (option == 4) {
                // Exit
                printf("Thank you for using the ATM. Goodbye!\n");
                break;
            } else {
                // Invalid option
                printf("Invalid option. Please try again.\n");
            }
        }
    }
    
    else {
        printf("Too many incorrect attempts. Exiting...\n");
    }

    return 0;
}
