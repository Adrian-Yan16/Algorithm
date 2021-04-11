class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        # 当前位置的值只与上面及左面的值有关
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


s = Solution()
print(s.uniquePaths(3,2))