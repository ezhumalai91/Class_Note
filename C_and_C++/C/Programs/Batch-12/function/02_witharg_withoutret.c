//amstrong Number
#include<stdio.h>
#include<conio.h>
int amstrong(int);
int amstrong(int n)
{
    int sum=0,rem;
    int temp=n;
    while(temp!=0)
    {
        rem=temp%10;
        sum+=rem*rem*rem;
        temp=temp/10;
    }
    if(sum==n)
    {
        printf("It is amstrong Number");
    }
    else{
        printf("It is not amstrong Number");
    }
}
int main()
{
    int n;
    printf("Enter a number:");
    scanf("%d",&n);
    amstrong(n);
}