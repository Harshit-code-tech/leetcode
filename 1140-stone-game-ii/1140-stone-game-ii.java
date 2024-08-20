class Solution {
    private int[] prefixSum;
    private int[][] memo;

    public int stoneGameII(int[] piles) {
        int n = piles.length;
        prefixSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + piles[i];
        }

        memo = new int[n][n + 1];
        return dfs(0, 1);
    }

    private int dfs(int i, int M) {
        if (i >= prefixSum.length - 1) return 0;
        if (2 * M >= prefixSum.length - i - 1) return prefixSum[prefixSum.length - 1] - prefixSum[i];
        if (memo[i][M] != 0) return memo[i][M];

        int result = 0;
        for (int x = 1; x <= 2 * M; x++) {
            int next = dfs(i + x, Math.max(M, x));
            result = Math.max(result, prefixSum[prefixSum.length - 1] - prefixSum[i] - next);
        }

        memo[i][M] = result;
        return result;
    }
}