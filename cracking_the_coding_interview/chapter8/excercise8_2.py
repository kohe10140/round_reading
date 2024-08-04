class Solution:

    def __init__(self):
        pass

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        self.path_grid = [[None for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        self.obstacleGrid = obstacleGrid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.rec(m-1, n-1)
        if self.obstacleGrid[0][0] == 1:
            return 0
        print(self.path_grid)
        return self.path_grid[m-1][n-1]
    
    def rec(self, i, j):
        if i == j == 0:
            self.path_grid[i][j] = 1
            return
        if self.obstacleGrid[i][j] == 1:
            self.path_grid[i][j] = 0
            return
        if i == 0:
            if self.path_grid[i][j-1] is None:
                self.rec(i, j-1)
            self.path_grid[i][j] = self.path_grid[i][j-1]
        elif j == 0:
            if self.path_grid[i-1][j] is None:
                self.rec(i-1, j)
            self.path_grid[i][j] = self.path_grid[i-1][j]
        else:
            if self.path_grid[i][j-1] is None:
                self.rec(i, j-1)
            if self.path_grid[i-1][j] is None:
                self.rec(i-1, j)
            self.path_grid[i][j] = self.path_grid[i-1][j] + self.path_grid[i][j-1]





s = Solution()

og = [[0, 1, 0], [0, 0, 0]]
print(s.uniquePathsWithObstacles(og))
og = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(s.uniquePathsWithObstacles(og))
og = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(s.uniquePathsWithObstacles(og))