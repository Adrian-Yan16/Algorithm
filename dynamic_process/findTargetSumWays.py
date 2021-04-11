class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        sum_p = (S + sum(nums))
        if sum_p % 2 != 0:
            return 0
        sum_p = sum_p // 2
        dp = [0] * (sum_p + 1)
        dp[0] = 1
        for j in nums:
            for i in range(sum_p,j - 1,-1):
                dp[i] += dp[i- j]
        return dp[-1]

s = Solution()
print(s.findTargetSumWays([1,2,7,9,981],
1000000000))