// #include <stdio.h>
// #include<conio.h>
// void display();

// void display(){
//     printf("Good Morning");
// }

// int main(){

//     display();
//     printf("Have a nice day");
//     return 0;
// }

// #include <stdio.h>
// #include<conio.h>
// int add_or_even();

// int add_or_even(){
//     int n;
//     printf("Enter a number: ");
//     scanf("%d",&n);
//     if(n%2==0){
//         return 1;
//         }
//         else{
//             return 0;
//             }
//             }



// int main(){

//     if (add_or_even()){
//         printf("Even number");
//     }
//     else{
//         printf("Odd number");
//     }
    
//     return 0;
// }



// #include <stdio.h>
// #include<conio.h>
// int add_or_even(int);

// int add_or_even(int n){
//     if(n%2==0){
//         return 1;
//         }
//         else{
//             return 0;
//             }
//             }



// int main(){
//     int n;
//     printf("Enter a number: ");
//     scanf("%d",&n);

//     if (add_or_even(n)){
//         printf("Even number");
//     }
//     else{
//         printf("Odd number");
//     }
    
//     return 0;
// }

#include <stdio.h>
#include<conio.h>
int add_or_even(int);

int add_or_even(int n){
    if(n%2==0){
        printf("Even");
        
        }
        else{
            printf("Odd");
            }
            }



int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);

    add_or_even(n);
    return 0;
}