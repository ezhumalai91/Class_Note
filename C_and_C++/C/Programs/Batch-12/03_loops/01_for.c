// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i;
    
//     printf("Enter any number:");
//     scanf("%d",&n);
//     for(i=0;i<n;i++)
//     {
//         printf("C Program\n");        
//     }

// }


// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i;
//     printf("***N Natural Number***");
//     printf("Enter any number:");
//     scanf("%d",&n);
//     for(i=1;i<=n;i++)
//     {
//         printf("%d\n",i);        
//     }

// }

// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i;
    
//     printf("Enter any number:");
//     scanf("%d",&n);
//     printf("Even numbers are :\n");
    
//     for(i=1;i<=n;i++)
//     {
//         if(i%2==0)        
//         {
//         printf("%d\n",i);
//         }        
//     }
// }

// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i;
    
//     printf("Enter any number:");
//     scanf("%d",&n);
//     printf("Odd numbers are :\n");
//     for(i=1;i<=n;i++)
//     {
//         if(i%2!=0)
//         {
//         printf("%d\n",i);
//         }        
//     }
// }

// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i,sum=0;
    
//     printf("***Sum of N Natural numbers***\n\n");
//     printf("Enter any number:");
//     scanf("%d",&n); //10   
//     for(i=1;i<=n;i++)
//     {
//          sum+=i;         
//     }
//     printf("The Sum of N number is %d",sum);

// }


// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int n,i,fact=1;
    
//     printf("***Factorial***\n\n");
//     printf("Enter any number:");
//     scanf("%d",&n);    
//     for(i=1;i<=n;i++)
//     {
//          fact*=i;         
//     }
//     printf("%d factorial is %d",n,fact);

// }



// #include <stdio.h>

// void main() {
//     char ch;
//     printf("Alphabets from A to Z:\n");
//     for (ch = 'A'; ch <= 'Z'; ++ch) {        
//         printf("%c\n", ch);
//     }        
// }


// break and continue

// Break:
//     break statement is a control flow statement used to terminate the execution of a loop.

#include<stdio.h>
#include<conio.h>

void main()
{
    int n,i;
    printf("***N Natural Number***");
    printf("Enter any number:");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        if(i==6)
        {
            break;
        }
        printf("%d\n",i);        
    }

}

// continue:
//     continue statement in C is a jump statement used within loops to skip the remaining part of the current iteration and proceed directly to the next iteration. 


#include<stdio.h>
#include<conio.h>

void main()
{
    int n,i;
    printf("***N Natural Number***");
    printf("Enter any number:");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        if(i==6)
        {
            continue;
        }
        printf("%d\n",i);        
    }

}








