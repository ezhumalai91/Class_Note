//Give a fastest way to multiply any number by 9.
#include<stdio.h>
#include<conio.h>
void main()
{
int n;
printf("Enter a number:");
scanf("%d",&n);
printf("%d", (n<<3)+n);
getch();
}