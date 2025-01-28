class Solution {
    public int findMaxFish(int[][] grid) {
        int maxFish = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] > 0 && !visited[r][c]) {
                    maxFish = Math.max(maxFish, dfs(grid, visited, r, c));
                }
            }
        }
        
        return maxFish;
    }

    private int dfs(int[][] grid, boolean[][] visited, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || visited[r][c] || grid[r][c] == 0) {
            return 0;
        }

        visited[r][c] = true;
        int fishCount = grid[r][c];
        fishCount += dfs(grid, visited, r + 1, c);
        fishCount += dfs(grid, visited, r - 1, c);
        fishCount += dfs(grid, visited, r, c + 1);
        fishCount += dfs(grid, visited, r, c - 1);

        return fishCount;
    }
}