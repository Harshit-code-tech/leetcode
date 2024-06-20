class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int prev1 = cost[0]; 
        int prev2 = 0; 
        for (int i = 1; i < n; i++) {
            int curr = cost[i] + Math.min(prev1, prev2); 
            prev2 = prev1;
            prev1 = curr;
        }
        return Math.min(prev1, prev2); 
    }
}
