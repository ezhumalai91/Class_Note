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

class child1 : public parent
{
   public:
     int y;
   public:
   void getinput()
   {
     cout << "Enter the value of y = ";
     cin >> y;
   }
 };

class child2 : public parent    //single derived class
{
  public:
   void display()
   {    
     cout << "The value of X is"<<x;
    }

 };
 
 int main()
 {
    child1 a;
    child2 b;    //object of derived class
    a.getdata();
    a.getinput();
    b.display();
    return 0;
 }