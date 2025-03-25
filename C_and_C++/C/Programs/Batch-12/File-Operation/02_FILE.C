#include <stdio.h>

int main() {
    FILE *outfile;
    char fname[20];
    
    printf("Enter the filename: ");
    scanf("%s", fname);
    
    outfile = fopen(fname, "w");
    if (outfile == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    
    fprintf(outfile, "Sujith\n");
    fprintf(outfile, "I am studying engineering\n");
    fprintf(outfile, "Vijay\n");
    fprintf(outfile, "Santhosh\n");
    printf("\nSuccessfully created\n");
    
    fclose(outfile);
    
    return 0;
}
