class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int prev1 = cost[0]; // Minimum cost for first stair
        int prev2 = 0; // Minimum cost for starting below stairs

        for (int i = 1; i < n; i++) {
            int curr = cost[i] + Math.min(prev1, prev2); // Calculate current cost
            prev2 = prev1; // Shift previous costs
            prev1 = curr;
        }

        return Math.min(prev1, prev2); // Minimum cost from last or second-to-last stair
    }
}
