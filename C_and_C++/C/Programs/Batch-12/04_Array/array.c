// #include <stdio.h>
// #include<conio.h>
// int main()
// {
//     int arr[5] = { 10, 20, 30, 40, 50 };
//     printf("%d",arr[0]);
//     printf("%d",arr[3]);

// return 0;
// }

// #include <stdio.h>
// #include<conio.h>
// int main()
// {
//     int arr[10] = { 10, 20, 30, 40, 15,5,3,2,7,1 },i;    
    
//     for(i=0;i<10;i++)
//     {
//         printf("%d\n",arr[i]);
//     }

// return 0;
// }


// #include <stdio.h>
// #include<conio.h>
// int main()
// {
//     int arr[3],i;
//     for(i=0;i<3;i++)
//     {
//         printf("Enter element %d :\t",i+1);
//         scanf("%d",&arr[i]);
//     }
//     for(i=0;i<3;i++)
//     {
//     printf("Element %d is %d\n",i+1,arr[i]);
//     }
//  return 0;   
// }

// #include <stdio.h>
// #include<conio.h>
// int main()
// {
//     int n,i;
//     printf("Enter the number of elements:\t");
//     scanf("%d",&n);
//     int arr[n];
//     for(i=0;i<n;i++)
//     {
//         printf("Enter element %d :\t",i+1);
//         scanf("%d",&arr[i]);
//         }
//         for(i=0;i<n;i++)
//         {
//             printf("Element %d is %d\n",i+1,arr[i]);
//         }

//  return 0;   
// }


// Two di
#include <stdio.h>
#include<conio.h>
int main()
{
    int arr[3][3];
    int i, j;

    // Input elements into the matrix
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 3; j++)
        {
            printf("Enter element [%d][%d]:\t", i, j);
            scanf("%d", &arr[i][j]);
        }
    }

    // Display the elements of the matrix
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 3; j++)
        {
            printf("Element [%d][%d] is %d\n", i, j, arr[i][j]);
        }
    }

    return 0;   
}

// duplicate number

// #include<stdio.h>
// #include<conio.h>
// int main()
// {
//     int arr[10],i,j,n;
//     printf("Enter the number of elements:\t");
//     scanf("%d",&n);
//     printf("Enter %d elements:\n",n);
//     for(i=0;i<n;i++)
//     {
//         scanf("%d",&arr[i]);
//     }
//     for(i=0;i<n;i++)
//     {
//         for(j=i+1;j<n;j++)
//         {
//             if(arr[i]==arr[j])
//             {
//                 printf("Duplicate element is %d\n",arr[i]);
//             }
//             }
//             }
// return 0;
// }

