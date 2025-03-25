#include <iostream>

using namespace std;

//#pattern program
// 1
// 1 2
// 1 2 3

int main()
{
    int n;
    cout<<"Enter line count:";
    cin>>n;
    for(int i=1;i<n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            cout<<j<<" ";
        }
        cout<<endl;
    }

return 0;
}