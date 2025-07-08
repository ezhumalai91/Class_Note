#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 25, 67, 89, 45, 90, 12};
    

    int largest = arr[0]; // Assume the first element is the largest

    for (int i = 1; i < 7; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    cout << "The largest number is: " << largest << endl;
    return 0;
}
