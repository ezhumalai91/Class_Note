#include <iostream>
using namespace std;

int main() {

  int low, high, i;
  int is_prime = 1;

  cout << "Enter two numbers (intervals): ";
  cin >> low >> high;

  cout << "\nPrime numbers between " << low << " and " << high << " are: " << endl;

  while (low < high) {
    is_prime = 1;

    // 0 and 1 are not prime numbers
    if (low == 0 || low == 1) {
      is_prime = 0;
    }
 
    for (i = 2; i <= low/2; i++) {
      if (low % i == 0) {
        is_prime = 0;
        break;
      }
    }
        
    if (is_prime)
      cout << low << ", ";

    low++;
  }

  return 0;
}