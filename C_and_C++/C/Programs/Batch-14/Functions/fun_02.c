// Arg and No return 

#include<stdio.h>
#include<conio.h>
void add(int,int);

void add(int a, int b){
    int sum;
    sum = a + b;
    printf("The addition of %d and %d is %d",a,b,sum);
}

int main (){
    int a,b;    
    printf("Enter the first number: ");
    scanf("%d",&a);
    printf("Enter the second number: ");
    scanf("%d",&b);
    add(a,b);
    return 0;
}