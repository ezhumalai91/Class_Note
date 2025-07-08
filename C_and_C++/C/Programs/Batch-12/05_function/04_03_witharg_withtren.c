#include<stdio.h>
#include<conio.h>
int sum(int,int);

int sum(int a,int b)
{
    int c;
    c=a+b;
    return c;
}

int main()
{
    int a,b,c;
    clrscr();
    printf("Please enter the values a and b:");
    scanf("%d%d",&a,&b);
    print("The Addition is %d",sum(a,b));
    
}