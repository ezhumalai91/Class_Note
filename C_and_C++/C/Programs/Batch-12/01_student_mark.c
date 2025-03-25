#include<stdio.h>
#include<conio.h>
void main()
{
    int t,e,m,s,ss,tol;
    float avg;

    printf("Please enter the Student marks:");
    scanf("%d\n%d\n%d\n%d\n%d",&t,&e,&m,&s,&ss);
    tol=t+e+m+s+ss;
    avg=tol/5;
    printf("\nTotal is\t:\t%d",tol);
    printf("\nAverage is\t:\t%f",avg);
        
}