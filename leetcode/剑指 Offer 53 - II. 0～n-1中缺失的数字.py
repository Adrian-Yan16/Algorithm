class Solution:
    def missingNumber(self, nums) -> int:
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                return nums[i] - 1
        if 0 in nums:
            return len(nums)
        return 0

    # 二分
    def missingNumber2(self, nums) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid
        return l

    def missingNumber3(self, nums) -> int:
        for idx,num in enumerate(nums):
            if idx != num:
                return idx
        return len(nums)

    def missingNumber4(self, nums) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)



if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber2([0,1,2,3,4,5,6,7,9]))
