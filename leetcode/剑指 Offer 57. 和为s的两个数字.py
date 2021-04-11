class Solution:
    # 暴力
    def twoSum(self, nums, target: int):
        diffirences = [target - nums[0]]
        for num in nums[1:]:
            diffir = target - num
            if num in diffirences:
                return [num,diffir]
            diffirences.append(diffir)
        return []

    # 指针
    def twoSum1(self, nums, target: int):
        if not nums:
            return []
        l = 0
        r = len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return [nums[l],nums[r]]
            elif sum < target:
                l += 1
            else:
                r -= 1
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum1(nums = [10,26,30,31,47,60], target = 40))