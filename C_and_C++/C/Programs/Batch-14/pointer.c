#include<stdio.h>
#include<conio.h>
void main()
{
int n=10;
int *ptr;
ptr=&n;
printf("Value of n is %d",n);
printf("\nAddress of n is %u",&n);
printf("\nAddres of pointer is %x",ptr);
printf("\nvalue stored in pointer is %d",*ptr);
printf("\nAddress of pointer n is %x",&n);
getch();
}
