#include <stdio.h>

int main() {
    FILE *outfile;
    char fname[] = "sample.txt";

    outfile = fopen(fname, "w");
    if (outfile == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(outfile, "hi\n");

    printf("Successfully added to %s\n", fname);

  
    fclose(outfile);

    return 0;
}
