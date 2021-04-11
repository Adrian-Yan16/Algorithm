class Solution:
    def wiggleMaxLength(self, nums) -> int:
        l = len(nums)
        if l <= 1:
            return l
        up = [nums[0]]
        down = [nums[0]]
        for i in range(1,l):
            if nums[i] > nums[i - 1]:
                up = down + [nums[i]]
            elif nums[i] < nums[i - 1]:
                down = up + [nums[i]]
        return max(len(up),len(down))

    def wiggleMaxLength_ft(self, nums) -> int:
        l = len(nums)
        if l <= 1:
            return l
        up = 1
        down = 1
        for i in range(1, l):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up,down)





s = Solution()
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))

