class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        res = grid[0]
        for i in range(row):
            for j in range(column):
                if i == 0 and j == 0:
                    res[j] = grid[i][j]
                    continue
                if i == 0:
                    res[j] += res[j - 1]
                    continue
                if j == 0:
                    res[j] += grid[i][j]
                    continue
                else:
                    res[j] = min(res[j - 1] + grid[i][j], res[j] + grid[i][j])
                    continue
        return res[-1]

