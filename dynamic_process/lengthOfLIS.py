class Solution:
    def lengthOfLIS(self, nums) -> int:
        l = len(nums)
        if l <= 1:
            return l
        dp = [1] * (l)
        for i in range(1,l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)

    def lengthOfLIS_ft(self, nums) -> int:
        l = len(nums)
        if l <= 1:
            return l
        tail,res = [0] * l,0
        for num in nums:
            i,j = 0,res
            while i < j:
                mid = (i + j) // 2
                if tail[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tail[i] = num
            if j == res:
                res += 1
        return res




s = Solution()
print(s.lengthOfLIS_ft([10,9,2,5,3,7,101,18]))

