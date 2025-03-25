#include <stdio.h>

int numWaterBottles(int numBottles, int emptyExchange) {
    int ans = numBottles;
    while (numBottles >= emptyExchange) {
        int full = numBottles / emptyExchange;
        int empty = numBottles % emptyExchange;
        ans += full;
        numBottles = full + empty;
    }
    return ans;
}

int main() {
    int numBottles = 12;
    int emptyExchange = 3;

    int result = numWaterBottles(numBottles, emptyExchange);
    printf("Total number of bottles you can drink: %d\n", result);

    return 0;
}
