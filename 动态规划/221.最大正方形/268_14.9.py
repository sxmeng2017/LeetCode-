class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        width, length = len(matrix), len(matrix[0])
        max_side = 0
        dp = [[0 for i in range(length)] for j in range(width)]
        for i in range(width):
            for j in range(length):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side**2