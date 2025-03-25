#include <stdio.h>
struct employee
{
    int empno;
    char empname[20];
    char deptname[10];
    float salary;
} emp[5];
int main() {
    for(int i = 0; i < 5; i++) {
        printf("Enter details for employee %d:\n", i + 1);
        printf("Employee Number: ");
        scanf("%d", &emp[i].empno);
        printf("Employee Name: ");
 
        while (getchar() != '\n');  // to clear newline left by previous input
        fgets(emp[i].empname, 20, stdin);
        // size_t len = strlen(emp[i].empname);
        // if (len > 0 && emp[i].empname[len - 1] == '\n') {
        //     emp[i].empname[len - 1] = '\0';
        // }
       
       printf("Department Name: ");
        fgets(emp[i].deptname, 10, stdin);
        // len = strlen(emp[i].deptname);
        // if (len > 0 && emp[i].deptname[len - 1] == '\n') {
        //     emp[i].deptname[len - 1] = '\0';
        // }

        printf("Salary: ");
        scanf("%f", &emp[i].salary);

        printf("\n");
    }
    printf("Employee Details:\n");
    for(int i = 0; i < 5; i++) {
        printf("Employee Number: %d\n", emp[i].empno);
        printf("Employee Name: %s\n", emp[i].empname);
        printf("Department Name: %s\n", emp[i].deptname);
        printf("Salary: %.2f\n", emp[i].salary);
        printf("\n");
    }

    return 0;
}