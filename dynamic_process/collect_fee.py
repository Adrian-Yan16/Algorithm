import sys

# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。输入: coins = [1, 2, 5], amount = 11，输出: 3
# 解释: 11 = 5 + 5 + 1 输入: coins = [2], amount = 3，输出: -
class Solution:
    dict_ = {}
    def exchange_rec(self,amount,coins):
        if amount in self.dict_:
            return self.dict_[amount]
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        res = sys.maxsize
        for i in range(len(coins)):
            submin = self.exchange_rec(amount - coins[i],coins)
            if submin == -1:
                continue
            res = min(submin + 1,res)
            self.dict_[amount] = res
        if res == sys.maxsize:
            return -1

        return res

    def exchange_dp(self,amount,coins):
        if amount == 0:
            return 0
        l = len(coins)
        if l == 0:
            return -1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for j in coins:
            for i in range(j, amount + 1):
                dp[i] = min(dp[i], dp[i - j] + 1)
        if dp[-1] == amount + 1:
            return -1
        return dp[-1]




s = Solution()
print(s.exchange_dp(11,[1,2,5]))