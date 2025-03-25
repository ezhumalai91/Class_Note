t numWaterBottles(int numBottles, int numExchange) {
    int ans = numBottles;
    while (numBottles >= numExchange) {
        int full = numBottles / numExchange;
        int empty = numBottles % numExchange;
        ans += full;
        numBottles = full + empty;