class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        int[][] dp = new int[n][k];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], 1); 
            
            for (int j = 0; j < i; j++) {
                int remainder = (nums[i] + nums[j]) % k;
                dp[i][remainder] = Math.max(dp[i][remainder], dp[j][remainder] + 1);
            }
        }
        int maxLength = 0;
        for (int[] row : dp) {
            for (int length : row) {
                maxLength = Math.max(maxLength, length);
            }
        }
        
        return maxLength;
    }

}
