#include <stdio.h>
#define SIZE 3

int main() {
    int first[SIZE][SIZE], second[SIZE][SIZE], result[SIZE][SIZE];

    // Input for the first 3x3 matrix
    printf("Enter elements of the first 3x3 matrix:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            scanf("%d", &first[i][j]);
        }
    }

    // Input for the second 3x3 matrix
    printf("Enter elements of the second 3x3 matrix:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            scanf("%d", &second[i][j]);
        }
    }

    // Call function to multiply matrices
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            result[i][j] = 0;  // Initialize result cell
            for (int k = 0; k < SIZE; k++) {
                result[i][j] += first[i][k] * second[k][j];  // Multiply and accumulate
            }
        }
    }

    // Print the result
    printf("Resultant Matrix:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    return 0;
}
