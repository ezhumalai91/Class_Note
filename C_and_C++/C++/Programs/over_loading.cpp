#include<iostream>
using namespace std;

int add(int,int);
int add(int,int,int);
int add(int,int,int,int);


int add(int a,int b){
    return a+b;
}
int add(int a,int b,int c){
    return a+b+c;
}

int add(int a,int b,int c,int d){
    return a+b+c+d;
}
int main(){
    cout<<add(5,8)<<endl;
    cout<<add(5,8,3)<<endl;
    cout<<add(5,8,3,55)<<endl;
return 0;
}