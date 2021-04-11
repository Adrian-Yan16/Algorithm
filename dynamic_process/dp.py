import copy
class Triangle:
    def __init__(self,triangle):
        self.triangle = triangle
        self.dict_ = {}

    def triangle_sum_rec(self,i,j):
        if not self.triangle:
            return 0
        if i >= len(self.triangle):
            return 0
        key = '%d%d'%(i,j)
        if key in self.dict_:
            return self.dict_[key]
        res = self.triangle[i][j]
        left = self.triangle_sum_rec(i+1,j)
        right = self.triangle_sum_rec(i+1,j+1)
        if left > right:
            res += right
        else:
            res += left
        self.dict_[key] = res
        return res

    def triangle_sum_dp(self):
        if not self.triangle:
            return 0
        dp = copy.deepcopy(self.triangle[-1])
        for i in range(len(self.triangle)-2,-1,-1):
            for j in range(i+1):
                if dp[j] < dp[j+1]:
                    dp[j] = self.triangle[i][j] + dp[j]
                else:
                    dp[j] = self.triangle[i][j] + dp[j+1]
        return dp[0]

class Fee:
    dict_ = {}
    def collect_fee_rec(self,amount,coins):
        if amount in self.dict_:
            return self.dict_[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = amount + 1
        for i in range(len(coins)):
            temp = self.collect_fee_rec(amount-coins[i],coins)
            if temp == -1:
                continue
            res = min(res,temp + 1)
        self.dict_[amount] = res
        if res == amount + 1:
            return -1
        return res

    def collect_fee_dp(self,amount,coins):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i],dp[i - coins[j]] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]


class StoneGame:
    def pick_stones(self,stones):
        if not stones:
            return (0,0)
        dp = [[[0,0] for i in range(len(stones))] for i in range(len(stones))]
        for i in range(len(stones)):
            dp[i][i][0] = stones[i]
        for l in range(2,len(stones) + 1):
            for i in range(len(stones) - l + 1):
                j = l + i - 1
                left = stones[i] + dp[i + 1][j][1]
                right = stones[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        return abs(dp[0][-1][0] - dp[0][-1][1])

class ThrowEggs:
    dict_ = {}
    def throw_egg(self,K,N):
        if K == 1:
            return N
        if N == 0:
            return 0
        key = '%d%d'%(K,N)
        if key in self.dict_:
            return self.dict_[key]
        res = float('INF')
        for k in range(1,K + 1):
            for n in range(1,N+1):
                left = self.throw_egg(k - 1,n - 1) + 1
                right = self.throw_egg(k,N - n) + 1
                if left < right:
                    res = min(res,right)
                else:
                    res = min(res,left)
        self.dict_[key] = res
        return res

    def throw_egg_dp(self,K,N):
        import sys
        if K == 1:
            return N
        if N == 0:
            return 0
        dp = [[0] * (N + 1) for i in range(K + 1)]
        for i in range(K + 1):
            for j in range(N + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif i == 1:
                    dp[i][j] = j
                else:
                    dp[i][j] = sys.maxsize
        for k in range(2,K+1):
            for n in range(1,N+1):
                # 从每层楼往下丢的情况
                for i in range(1,n+1):
                    dp[k][n] = min(dp[k][n],max(
                        dp[k - 1][i - 1],
                        dp[k][n - i]
                    ) + 1)
        return dp[K][N]







# triangle = [
#     [2, 0, 0, 0],
#     [3, 4, 0, 0],
#     [6, 5, 7, 0],
#     [0, 1, 8, 3]
# ]
# s = Triangle(triangle)
# print(s.triangle_sum_rec(0,0))
# print(s.triangle_sum_dp())

# s = Fee()
# print(s.collect_fee_dp(5,[2]))

# s = StoneGame()
# print(s.pick_stones([3,9,1,2]))
s = ThrowEggs()
print(s.throw_egg_dp(2,100))
