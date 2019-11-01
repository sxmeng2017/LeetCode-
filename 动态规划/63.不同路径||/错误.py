class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        temp = [[0] * columns] * rows
        for i in range(rows):
            for j in range(columns):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    temp[i][j] = 1
                    continue
                if i == 0:
                    temp[i][j] = temp[i][j - 1]
                    continue
                if j == 0:
                    temp[i][j] = temp[i - 1][j]
                    continue
                if obstacleGrid[i][j - 1] == 1 and temp[i - 1][j]:
                    temp[i][j] = temp[i - 1][j]
                    continue
                if obstacleGrid[i - 1][j] == 1 and temp[i][j - 1]:
                    temp[i][j] = temp[i][j - 1]
                    continue
                temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
        return temp[-1][-1]
