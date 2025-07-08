#include<stdio.h>
#include<conio.h>
#include<string.h>
void string_cpy(char []);


void string_cpy(char str1[])
{
    char str2[20];
    printf("%s",str1);
    
    strcpy(str2,str1);
    printf("After copy of string\n");
    printf("Str2 = %s",str2);

}


void main()
{
    char str1[20];
    int ch;
    while(1)
    {
        printf("1. String copy\n2. String Compare    5. Exit");
        printf("Please enter any of you choice");
        scanf("%d",&ch);
        if(ch==1)
        {
            printf("Enter the string\n");
            gets(str1);
            string_cpy(str1);

        }
        else if(ch==2)
        {

        }
else if(ch==4)
        {
            break;

        }

    }
 
    
}