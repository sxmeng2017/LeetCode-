class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1] * m] + [[1] + [0] * (m-1)] * (n - 1)
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i][j-1] + res[i-1][j]
        return res[-1][-1]