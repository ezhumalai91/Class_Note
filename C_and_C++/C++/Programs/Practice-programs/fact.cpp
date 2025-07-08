#include <iostream>
using namespace std;

int main()
{
int n,i,fact=1;
cout << "Enter the number of elements: ";
cin >> n;

for(i=n;i>=1;i--)
{
    fact=fact*i;
}
cout<<fact;
}