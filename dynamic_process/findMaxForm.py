class Solution:
    def findMaxForm(self, strs, m: int, n: int):
        l = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in strs:
            zeros = i.count('0')
            ones = i.count('1')
            for k in range(m,zeros - 1,-1):
                for j in range(n,ones - 1,-1):
                    dp[k][j] = max(dp[k][j],dp[k - zeros][j - ones] + 1)
        return dp[m][n]




s = Solution()
print(s.findMaxForm(["10", "0001", "111001", "1", "0"],5,3))
