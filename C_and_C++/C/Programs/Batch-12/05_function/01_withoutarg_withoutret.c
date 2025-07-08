// #include<stdio.h>
// #include<conio.h>
// void hi();

// void hi()
// {
//     printf("Good morning");
// }

// void main()
// {
//     hi();    
//     hi();
//     hi();

// }


#include<stdio.h>
#include<conio.h>
void add();

void add()
{
    int a,b,c;
    printf("Enter two numbers\n");
    scanf("%d%d",&a,&b);
    c=a+b;
    printf("Sum of two numbers is %d",c);
}

void main()
{
    add(); //function calling
}