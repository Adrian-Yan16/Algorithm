class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.count = 0
        self.judge(m,n,0,0)
        return self.count

    def judge(self,rows,cols,i,j):
        if i >= rows or j >= cols or i < 0 or j < 0:
            return 0
        if i == rows - 1 and j == cols - 1:
            self.count += 1
        self.judge(rows,cols,i,j + 1)
        self.judge(rows,cols,i + 1,j)

    def uniquePaths_dp(self, m: int, n: int) -> int:
        # 定义dp[i][j]为到i，j这个位置的最多路径
        # 状态转移为dp[i][j]=dp[i-1][j] + dp[i][j-1]
        dp = [1] * n
        for j in range(1,m):
            for i in range(1,n):
                dp[i] += dp[i - 1]
        return dp[-1]

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i - 1 < 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j - 1 < 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
        return obstacleGrid[-1][-1]



s = Solution()
list_ = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(s.uniquePathsWithObstacles(list_))