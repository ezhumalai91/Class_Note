#include <stdio.h>
#include<conio.h>
// int main() {

// int a[]={3,4,6,3,6,7};
// printf("%d",a[1]);
//     return 0;
// }

int main() {

int a[30],n,i;
printf("How many elements need get from user\t:");
scanf("%d",&n);
for(i=0;i<n;i++)
{
    printf("Enter the value %d:\t",i+1);
    scanf("%d",&a[i]);
}

for (i = 0; i < n; i++)
{
printf("Value %d:\t%d\n",i+1, a[i]);
}

return 0;
}