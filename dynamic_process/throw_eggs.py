import sys
class Solution:
    dict_ = {}
    def throw_eggs_rec(self,k,n):
        if k == 1:
            return n
        if n == 0:
            return 0
        key = '%d%d'%(k,n)
        if key in self.dict_:
            return self.dict_[key]
        res = float('INF')
        for i in range(1,n + 1):
            res = min(res,max(
                self.throw_eggs_rec(k-1,i - 1),
                self.throw_eggs_rec(k,n-i)
            ) + 1)
        self.dict_[key] = res
        return res

    def throw_eggs_dp(self, K, N):
        if K == 1:
            return N
        if N == 0:
            return 0
        dp = [[0] * (N + 1) for i in range(K + 1)]
        for i in range(K + 1):
            for j in range(N + 1):
                if i ==0 or j == 0:
                    dp[i][j] = 0
                elif i == 1:
                    dp[i][j] = j
                else:
                    dp[i][j] = sys.maxsize
        for k in range(2, K + 1):
            for n in range(1, N + 1):
                for i in range(1,N+1):
                    dp[k][n] = min(dp[k][n], max(
                        dp[k - 1][i - 1],
                        dp[k][n - i]
                    ) + 1)
        return dp[K][N]



s = Solution()
print(s.throw_eggs_dp(2,100))