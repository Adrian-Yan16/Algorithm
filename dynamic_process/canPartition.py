# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

class Solution:
    def canPartition(self, nums) -> bool:
        if len(nums) <= 1:
            return False
        if sum(nums) % 2 != 0:
            return False
        mid = sum(nums) // 2
        dp = [0] * (mid + 1)
        dp[0] = 1
        if nums[0] <= mid:
            dp[nums[0]] = 1
        for i in range(1,len(nums)):
            for j in range(mid,nums[i]-1,-1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1] == 1

    def can2(self,nums):
        if len(nums) <= 1:
            return False
        if sum(nums) % 2 != 0:
            return False
        mid = sum(nums) // 2
        s = set()
        s.add(mid)
        for i in nums:
            c = s.copy()
            for j in c:
                if j == i:
                    return True
                elif j > i:
                    s.add(j - i)
        return False




s= Solution()
print(s.can2([3,3,3,4,5]))