#include<stdio.h>
#include<conio.h>
int factorial(int);

int factorial(int num)
{
if(num>1)
    return(num*factorial(num-1));
else
    return(1);
}

void main(){
    int num;
    printf("enter the number:");
    scanf("%d",&num);
    printf("factorial of %d is %d",num,factorial(num));
    
}

// H/w

input--->10
output--->9+7+5+3+1===>
