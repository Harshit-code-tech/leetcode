class Solution {
    public int nthUglyNumber(int n) {
        if (n <= 0) return 0;
        
        int[] dp = new int[n];
        dp[0] = 1;
        int i2 = 0, i3 = 0, i5 = 0;
        
        for (int i = 1; i < n; i++) {
            int nextUgly = Math.min(dp[i2] * 2, Math.min(dp[i3] * 3, dp[i5] * 5));
            dp[i] = nextUgly;
            
            if (nextUgly == dp[i2] * 2) i2++;
            if (nextUgly == dp[i3] * 3) i3++;
            if (nextUgly == dp[i5] * 5) i5++;
        }
        
        return dp[n - 1];
    }
}
