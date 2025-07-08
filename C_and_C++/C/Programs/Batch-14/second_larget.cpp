#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 25, 67, 89, 45, 90, 12};
    int n = sizeof(arr) / sizeof(arr[0]);

    if (n < 2) {
        cout << "At least two numbers are required!" << endl;
        return 0;
    }

    int first = arr[0], second = arr[0];

    // Find the largest element first
    for (int i = 1; i < n; i++) {
        if (arr[i] > first) {
            first = arr[i];
        }
    }

    // Find the second largest element
    second = arr[0]; // Reset to first element
    for (int i = 0; i < n; i++) {
        if (arr[i] > second && arr[i] < first) {
            second = arr[i];
        }
    }

    if (first == second) {
        cout << "No second largest number found!" << endl;
    } else {
        cout << "The second largest number is: " << second << endl;
    }

    return 0;
}