class Solution:
    def minNumber(self, nums) -> str:
        l = len(nums)
        if l == 1:
            return str(nums[0])
        for i in range(l - 1):
            for j in range(i + 1,l):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    nums[i],nums[j] = nums[j],nums[i]
        strs = [str(i) for i in nums]
        return ''.join(strs)

    # 快排
    def minNumber2(self, nums) -> str:
        l = len(nums)
        if l == 1:
            return str(nums[0])

        def quick_sort(l,r):
            if l >= r:
                return
            i = l
            j = r

            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                strs[i],strs[j] = strs[j],strs[i]
            strs[i],strs[l] = strs[l],strs[i]
            quick_sort(0,i-1)
            quick_sort(i + 1,r)

        strs = [str(i) for i in nums]
        quick_sort(0,l - 1)
        return ''.join(strs)


if __name__ == '__main__':
    s = Solution()
    print(s.minNumber2([3,30,34,5,9]))

