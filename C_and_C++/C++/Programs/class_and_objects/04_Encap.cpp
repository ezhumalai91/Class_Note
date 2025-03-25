#include <iostream>
using namespace std;

class Rectangle {
   private:

    int length;
    int breadth;

   public:

    // Setter function for length
    void setLen_Breadth(int len, int brth) {
      length = len;
      breadth = brth;
    }

    // Getter function for length
    int getLength() {
      return length;
    }

    // Getter function for breadth
    int getBreadth() {
      return breadth;
    }
    // Function to calculate area
    int getArea() {
      return length * breadth;
    }
};

int main() {
  // Create object of Rectangle class
  Rectangle r;

  // Initialize length using Setter function
  r.setLen_Breadth(8,6);

  // Access length using Getter function
  cout << "Length = " << r.getLength() << endl<<"Breadth = " << r.getBreadth() << endl;
  // Call getArea() function
  cout << "Area = " << r.getArea();

  return 0;
}