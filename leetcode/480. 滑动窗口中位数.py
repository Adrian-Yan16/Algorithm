import bisect

class Solution:
    def medianSlidingWindow(self, nums, k: int):
        res = []
        if k %2 != 0:
            for i in range(len(nums) - k + 1):
                temp = sorted(nums[i:i + k])
                m = k // 2
                res.append(temp[m])
        else:
            for i in range(len(nums) - k + 1):
                temp = sorted(nums[i:i + k])
                m1 = k // 2 - 1
                m2 = k // 2
                res.append((temp[m1] + temp[m2]) / 2)
        return res

    # 数值 + 二分查找
    def medianSlidingWindow2(self, nums, k: int):
        l = len(nums)
        start = 0
        window = sorted(nums[:k])
        res = [window[k // 2] if k % 2 else (window[k // 2] + window[k // 2 - 1]) / 2]
        for i in range(k,l):
            bisect.insort(window,nums[i])
            window.pop(bisect.bisect_left(window,nums[start]))
            start += 1

            res.append(window[k // 2] if k % 2 else (window[k // 2] + window[k // 2 - 1]) / 2)
        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3

s = Solution()
print(s.medianSlidingWindow2(nums,k))
