#include <iostream> 
using namespace std; 
class parent1
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

class parent2
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

class child : public parent1,public parent2    //single derived class
{
   public:
    int sum;
   public:
   void add()
   {
    sum=x+y;
     cout << "The addition of x and y is = "<<sum;
        }

 };
 
 int main()
 {
    child a;     //object of derived class
    a.getdata();
    a.getinput();
    a.add();
    return 0;
 }