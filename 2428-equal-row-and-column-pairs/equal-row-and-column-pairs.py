class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        g_map = {}
        count = 0
        for row in grid:
            g_map[tuple(row)]= g_map.get(tuple(row),0)+1
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count+=g_map.get(tuple(col),0)
        return count