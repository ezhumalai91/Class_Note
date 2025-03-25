#include<stdio.h>
#include<conio.h>
void main()
{
    int a,b,c;
    printf("Enter the value of A,B and C:\t");
    scanf("%d%d%d",&a,&b,&c);
    if(a>b && a>c)
    {
        printf("\nA is the greater than B and C");
    }
    else if(b>a && b>c)
    {
        printf("\nB is the greater than A and C");
    }
    else
    {
        printf("\nC is the greater than A and B");
    }
}
    
    