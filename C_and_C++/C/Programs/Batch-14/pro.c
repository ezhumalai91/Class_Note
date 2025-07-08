#include<stdio.h>
#include<conio.h>
void main(){

    int arr[10],n,i;
    printf("Please enter the no of elements");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        printf("Enter element of arr[%d]",i);
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
    printf("value %d is %d \n",i,arr[i]);

    }
}