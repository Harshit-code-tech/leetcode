class Solution {
    public int minSteps(int n) {
        int step = 0;
        int x = 2;
        while (n > 1) {
            while (n % x == 0) {
                step += x;
                n /= x;
            }
            x++;
        }

        return step;
    }
}