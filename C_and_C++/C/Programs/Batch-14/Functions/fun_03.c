// No Arg and return 

#include<stdio.h>
int add();

int add(){
    int a,b,sum;    
    printf("Enter the first number: ");
    scanf("%d",&a);
    printf("Enter the second number: ");
    scanf("%d",&b);
    sum = a + b;
    return sum;
}

int main(){
    int result;
    result = add();
    printf("The addition of two number is %d",result);
    return 0;
}