class Solution:
    def stoneGame0(self,piles):
        if not piles:
            return 0
        if len(piles) <= 1:
            return piles[0]
        l = len(piles)
        dp = [[[0,0] for i in range(l)] for i in range(l)]
        for i in range(l):
            dp[i][i][0] = piles[i]
        for n in range(2,l+1):
            for i in range(l - n + 1):
                j = n + i - 1
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
        res = dp[0][l-1]
        return res[0] - res[1]

    def stoneGame(self, piles) -> bool:
        l = len(piles)
        dp = [[0] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = piles[i]
        for i in range(l - 2, -1,-1):
            for j in range(i + 1,l):
                dp[i][j] = max(piles[i] - dp[i + 1][j],piles[j] - dp[i][j - 1])
        return dp[0][l - 1] > 0

    def stoneGame2(self,piles):
        l = len(piles)
        dp = [i for i in piles]
        for i in range(l - 2,-1,-1):
            for j in range(i + 1,l):
                dp[i] = max(piles[i] - dp[i + 1],piles[j] - dp[j - 1])
        return dp[-1] > 0

s = Solution()
print(s.stoneGame([5,3,4,5]))
