#include <stdio.h>

struct employee {
    int empno;
    char empname[20];
    char deptname[10];
    float salary;
} emp[5];

int main() {
    // Loop to get input for 5 employees
    for(int i = 0; i < 5; i++) {
        printf("Enter details for employee %d:\n", i + 1);

        // Input employee number
        printf("Employee Number: ");
        scanf("%d", &emp[i].empno);

        // Clear the newline left by scanf
        while(getchar() != '\n');

        // Input employee name using gets
        printf("Employee Name: ");
        gets(emp[i].empname);  // Use gets to read the full name with spaces

        // Input department name using gets
        printf("Department Name: ");
        gets(emp[i].deptname);  // Use gets to read the department name with spaces

        // Input salary
        printf("Salary: ");
        scanf("%f", &emp[i].salary);

        printf("\n");
    }

    // Loop to print all the employee details
    printf("\nEmployee Details:\n");
    for(int i = 0; i < 5; i++) {
        printf("Employee %d:\n", i + 1);
        printf("Employee Number: %d\n", emp[i].empno);
        printf("Employee Name: %s\n", emp[i].empname);
        printf("Department Name: %s\n", emp[i].deptname);
        printf("Salary: %.2f\n", emp[i].salary);
        printf("\n");
    }

    return 0;
}
