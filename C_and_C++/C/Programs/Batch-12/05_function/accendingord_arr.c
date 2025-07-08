// //Accending order of array

// #include<stdio.h>
// #include<conio.h>
// void accending(int []);
// void accending(int n[])
// {
//     int i,j,temp;
//     for(i=0;i<5;i++)
//     {
//         for(j=i+1;j<5;j++)
//         {
//             if(n[i]>n[j])
//             {
//                 temp=n[i];
//                 n[i]=n[j];
//                 n[j]=temp;
//             }
//             }
//     }
//     printf("After Accending order");
//     for(i=0;i<5;i++)
//     {
//         printf("%d",n[i]);
//     }
// }

// void main()
// {
// int a[5]={3,6,2,8,1};

// accending(a);

// }

//Second largest number

#include<stdio.h>
#include<conio.h>
void accending(int [],int);
void accending(int n[],int length)
{
    printf("%d",length);
    int i,j,temp;
    for(i=0;i<length;i++)
    {
        for(j=i+1;j<length;j++)
        {
            if(n[i]>n[j])
            {
                temp=n[i];
                n[i]=n[j];
                n[j]=temp;
            }
            }
    }
    printf("After Accending order");
    for(i=0;i<length;i++)
    {
        printf("%d",n[i]);
    }
    printf("Second largest number is %d",n[length-2]);
}

void main()
{
int a[5]={3,6,2,8,1},length;
length=sizeof(a) / sizeof(a[0]);
accending(a,length);
}

