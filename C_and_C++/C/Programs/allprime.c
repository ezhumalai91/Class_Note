#include <stdio.h>

int main() {
    int limit, i, j, isPrime;

    printf("Enter a number: ");
    scanf("%d", &limit);

    printf("Prime numbers up to %d are:\n", limit);

    for (i = 2; i <= limit; i++) {
        isPrime = 1; // Assume the number is prime

        for (j = 2; j * j <= i; j++) { 
            if (i % j == 0) {
                isPrime = 0; // The number is not prime
                break;
            }
        }

        if (isPrime) {
            printf("%d ", i);
        }
    }
    printf("\n");

    return 0;
}
