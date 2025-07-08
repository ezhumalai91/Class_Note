// with Arg and with return type 

#include<stdio.h>
int add(int,int);

int add(int a,int b){
    int sum;
    sum = a + b;
    return sum;
}

int main(){
    int a,b,result;
    printf("Enter the first number: ");
    scanf("%d",&a);
    printf("Enter the second number: ");
    scanf("%d",&b);
    result = add(a,b);
    printf("The addition of two number is %d",result);
    return 0;
}