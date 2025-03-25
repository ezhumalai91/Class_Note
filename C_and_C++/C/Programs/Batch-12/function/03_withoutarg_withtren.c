#include<stdio.h>
#include<conio.h>
char duplicate();

char duplicate() {
    char arr[5] = {'e', 'i', 'b', 'e', 'z'};
    int i, j;
    for (i = 0; i < 5; i++) {
        for (j = i + 1; j < 5; j++) {
            if (arr[i] == arr[j]) {
                return arr[i];
            }
        }
    }
    return '\0';  // Return null character if no duplicate is found
}

void main() {
    char dup = duplicate();
    clrscr();
    if (dup != '\0') {
        printf("Duplicate character is %c\n", dup);
    } else {
        printf("No duplicate character found.\n");
    }
    
}