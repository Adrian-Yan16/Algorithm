class Solution:
    def maxSlidingWindow(self, nums, k: int):
        length = len(nums)
        if k > length:
            return []
        res = []
        # 维护当前窗口最大值的索引
        queue = []
        i = 0
        while i < length:
            # 当前位置已经超过queue[0]，就弹出
            if queue and i - k + 1 > queue[0]:
                queue.pop(0)
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i - k + 1 >= 0:
                res.append(nums[queue[0]])
            i += 1
        return res







s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))

