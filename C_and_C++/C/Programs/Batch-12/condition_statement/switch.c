#include<stdio.h>

int main() {
    char operation;
    double num1, num2;

    // Prompt user to enter an operation
    printf("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division");
    printf("Enter any choice: ");
    scanf("%d", &operation);

    // Prompt user to enter two numbers
    printf("Enter two numbers: ");
    scanf("%lf %lf", &num1, &num2);

    // Switch statement to perform the chosen operation
    switch (operation) {
        case 1:
            printf("Result: %.2lf\n", num1 + num2);
            break;
        case 2:
            printf("Result: %.2lf\n", num1 - num2);
            break;
        case 3:
            printf("Result: %.2lf\n", num1 * num2);
            break;
        case 4:
            if (num2 != 0) {
                printf("Result: %.2lf\n", num1 / num2);
            } else {
                printf("Error: Division by zero is not allowed.\n");
            }
            break;
        default:
            printf("Error: Invalid operation.\n");
            break;
    }

    return 0;
}
