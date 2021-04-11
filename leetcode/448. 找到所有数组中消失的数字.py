class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            tmp = nums[i]
            if nums[abs(tmp) - 1] > 0:
                nums[abs(tmp) - 1] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


s = Solution()
d = s.findDisappearedNumbers([4,3,2,7,1,2,3,1])
print(d)
