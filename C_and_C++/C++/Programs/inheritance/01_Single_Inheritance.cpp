#include <iostream> 
using namespace std; 
class parent
{
   public:
     int x;
   public:
   void getdata()
   {
     cout << "Enter the value of x = ";
     cin >> x;
   }
 };


class child : public parent    //single derived class
{
   public:
    int y;
   public:
   void readdata()
   {
     cout << "Enter the value of y = ";
     cin >> y;
   }
   void product()
   {
     cout << "Product = " << x * y;
   }
 };
 
 int main()
 {
    child a;     //object of derived class
    a.getdata();
    a.readdata();
    a.product();
    return 0;
 }