#include<stdio.h>
#include<conio.h>
void main()
{
    int n,i=1;
    
    printf("Enter any number:");
    scanf("%d",&n);
    do
    {
        printf("%d\n",i);
        i++;
    }while (i>=n);
 

}