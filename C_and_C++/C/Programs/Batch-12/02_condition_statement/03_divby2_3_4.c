#include<stdio.h>
#include<conio.h>
void main()
{
    int n;
    
    printf("Enter the any value:");
    scanf("%d",&n);
    if(n%2==0 && n%3==0 && n%4==0)
    {
        printf("%d is divisible by 2,3,4",n);
    }
    else
    {
        printf("%d is not divisible by 2,3,4",n);
    }
    
}