class Solution:
    # 记忆化搜索
    def stoneGameII(self, piles) -> int:
        l = len(piles)
        memory = {}
        # s表示第i堆及之后的石子总和
        s = [0] * (l + 1)
        for i in range(l - 1,-1,-1):
            s[i] = s[i + 1] + piles[i]
        def dfs(i,M):
            if (i,M) in memory:
                return memory[(i,M)]
            # 溢出
            if i >= l:
                return 0
            # 表示拿到剩下的所有石子
            if i + M * 2 >= l:
                return s[i]
            best = 0
            for x in range(1, M * 2 + 1):
                # 减去对方能拿到最大的值即为己方的最优策略
                best = max(best,s[i] - dfs(i + x,max(x,M)))
            memory[(i,M)] = best
            return best
        return dfs(0,1)
    
    def stoneGameII2(self, piles) -> int:
        l = len(piles)
        s = [0] * (l + 1)
        for i in range(l - 1, -1, -1):
            s[i] = s[i + 1] + piles[i]
        dp = [[0] * (l + 1) for _ in range(l + 1)]
        for i in range(l - 1,-1,-1):
            for M in range(l + 1):
                if i + M * 2 >= l:
                    dp[i][M] = s[i]
                    continue
                x = 1
                while x <= 2 * M:
                    dp[i][M] = max(dp[i][M],s[i] - dp[i + x][max(x,M)])
                    x += 1
        return dp[0][1]






s = Solution()
print(s.stoneGameII2([2,7,9,4,4]))
