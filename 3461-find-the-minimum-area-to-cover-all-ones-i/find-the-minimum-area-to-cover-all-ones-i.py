class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = [i for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
        cols = [j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
        return (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1)
