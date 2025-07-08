// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int i,j;
//     for(i=1;i<=5;i++)
//     {
//         for(j=1;j<=5;j++)
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
// }

// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int i,j;
//     for(i=1;i<=5;i++)
//     {
//         for(j=1;j<=5;j++)
//         {
//             if(j==1 || i==5 ||i==1 || j==5)
//             {
//             printf("*");
//             }
//             else
//             {
//             printf(" ");    
//             }
//         }
//         printf("\n");
//     }
// }


// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int i,j;
//     for(i=1;i<=5;i++)
//     {
//         for(j=1;j<=5;j++)
//         {
//             if(i==j || i+j==6)
//             {
//             printf("*");
//             }
//             else
//             {
//             printf(" ");    
//             }
//         }
//         printf("\n");
//     }
// }



// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int i,j;
//     for(i=1;i<=5;i++)
//     {
//         for(j=1;j<=5;j++)
//         {
//             if(i==j || i+j==6 || j==1 || i==5 ||i==1 || j==5)
//             {
//             printf("*");
//             }
//             else
//             {
//             printf(" ");    
//             }
//         }
//         printf("\n");
//     }
// }




// #include<stdio.h>
// #include<conio.h>
// void main()
// {
//     int i,j;
//     for(i=1;i<=5;i++)
//     {
//         for(j=1;j<=5;j++)
//         {
//             if(i==j || i+j==6 || j==1 || i==5 ||i==1 || j==5)
//             {
//             printf("*");
//             }
//             else
//             {
//             printf(" ");    
//             }
//         }
//         printf("\n");
//     }
// }

//to Print D

// #include <stdio.h>

// void main() {
//     int i, j;
//     for (i = 1; i <= 5; i++) {
//         for (j = 1; j <= 5; j++) {
//             if (j == 1 || (i == 1 && j < 5) || (i == 5 && j < 5) || (j == 5 && i != 1 && i != 5)) {
//                 printf("*");
//             } else {
//                 printf(" ");
//             }
//         }
//         printf("\n");
//     }
// }

//to Print S

// #include <stdio.h>

// void main() {
//     int i, j;
//     for (i = 1; i <= 5; i++) {
//         for (j = 1; j <= 5; j++) {
//             if (i == 1 || i==5 || i==3 ||( i!=4 && i!=5 && j==1)||(i!=1 && i!=2 && j==5))
//             {
//                 printf("|");
//             } else {
//                 printf(" ");
//             }
//         }
//         printf("\n");
//     }
// }



// *
// **
// ***
// ****
// *****

// #include <stdio.h>

// void main() {
//     int i, j;
//     int rows = 5; // Number of rows for the triangle
//     for (i = 1; i <= rows; i++) {
//         for (j = 1; j <= i; j++) {
//             printf("*");
//         }
//         printf("\n");
//     }
// }

//Opposite traiange
// #include <stdio.h>
// void main() {
//     int i, j;
//     int rows = 10; // Number of rows for the triangle
//     for (i = rows; i >= 1; i--) {
//         for (j = 1; j <= i; j++) {
//             printf("*");
//         }
//         printf("\n");
//     }
// }



//Tree

// #include <stdio.h>

// void main() {
//     int i, j;
//     int rows = 5; // Number of rows for the triangle
//     for (i = 1; i <= rows; i++) {
//         // Print leading spaces
//         for (j = i; j < rows; j++) {
//             printf(" ");
//         }
//         // Print stars
//         for (j = 1; j <= (2 * i - 1); j++) {
//             printf("*");
//         }
//         printf("\n");
//     }
// }



//Diamen
//     *
//    ***
//   *****
//  *******
// *********
//  *******
//   *****
//    ***
//     *

// #include <stdio.h>

// void main() {
//     int i, j;
//     int n = 5; // Number of rows for the top half of the diamond

//     // Top half of diamond
//     for (i = 1; i <= n; i++) {
//         for (j = i; j < n; j++) {
//             printf(" ");
//         }
//         for (j = 1; j <= (2 * i - 1); j++) {
//             printf("*");
//         }
//         printf("\n");
//     }

//     // Bottom half of diamond
//     for (i = n - 1; i >= 1; i--) {
//         for (j = n; j > i; j--) {
//             printf(" ");
//         }
//         for (j = 1; j <= (2 * i - 1); j++) {
//             printf("*");
//         }
//         printf("\n");
//     }
// }
