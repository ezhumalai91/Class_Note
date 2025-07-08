#include <iostream>
using namespace std;

int main()
{
int n,i,add=0;
cout << "Enter the number of elements: ";
cin >> n;

for(i=n;i>=1;i--)
{
    add=add+i;
}
cout<<add;
}