// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i=1;
    
//     printf("Enter any number:");
//     scanf("%d",&n);
//     while(i<=n)
//     {
//         printf("%d\n",i);
//         i++;
//     } 

// }

// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     char ch='a';
//     printf("\t\t*** A to Z Program***");
//     while(ch<='z')
//     {
//         printf("%c\n",ch);
//         ch++;
//     } 

// }

// o/p:
// 1 * 7 = 7
// 2 * 7 = 14
// ....

// #include<stdio.h>
// #include<conio.h>
// void main()
// {
// int tab,count,i=1;
// printf("\t\t***Table Program***\n\n");
// printf("Which table you want\t:");
// scanf("%d",&tab);
// printf("How many times you want to print\t:");
// scanf("%d",&count);

// while(i<=count)
// {
//     printf("%d * %d = %d\n",i,tab,i*tab);
//     i++;
// }
// }

// o/p:
// input   =  467
// output   =  764

#include<stdio.h>
#include<conio.h>
void main()
{
int n,remainder,reverse=0;

printf("\t\t***Reverse Number***\n\n");
printf("Enter any number:");
scanf("%d",&n);
while(n!=0)
{
    remainder=n%10;
    reverse=reverse*10+remainder;
    n=n/10;
}
printf("The Reverse number is %d",reverse);

}

// expalanation:
// n=467
// rem=7 rev=7 n=46
// rem=6 rev=76 n=4





//prime no

// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i;

//     printf("\t\t***Prime Number***\n\n");
//     printf("Enter any number:");
//     scanf("%d",&n);
//     for(i=2;i<n;i++)
//     {
//         if(n%i==0)
//         {
//             printf("It is not a prime number");
//             break;
//         }
//         else
//         {
//             printf("It is a prime number");
//             break;
//         }
//     }

// }

//swape two numbers
// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int a,b,temp;
//     printf("\t\t***Swap Two Numbers***\n\n");
//     printf("Enter first number:");
//     scanf("%d",&a);
//     printf("Enter second number:");
//     scanf("%d",&b);
//     printf("Before swapping:\n");
//     printf("a=%d and b=%d\n",a,b);
//     temp=a;
//     a=b;
//     b=temp;
//     printf("After swapping:\n");
//     printf("a=%d and b=%d\n",a,b);
// }

//fibnocii series(0 1 1 2 3 5 8 13 )
// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i=0,a=0,b=1,next_term;
//     printf("\t\t***Fibonacci Series***\n\n");
//     printf("Enter any number:");
//     scanf("%d",&n);
//     printf("Fibonacci Series is:\n");
//     printf("%d\n%d\n",a,b);
//     while(i<n)
//     {
//         next_term=a+b;
//         printf("%d\n",next_term);
//         a=b;
//         b=next_term;
//         i++;
//     }
// }



















