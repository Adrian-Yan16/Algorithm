class Solution:
    # 巧妙
    def reversePairs(self, nums) -> int:
        temp = sorted(nums)
        count = 0
        for j in temp:
            idx = nums.index(j)
            for i in range(idx):
                if j < nums[i]:
                    count += 1
            nums.pop(idx)
        return count

    # 归并
    def reversePairs2(self, nums) -> int:
        l = len(nums)
        if l < 2:
            return nums
        self.count = 0

        def merge(list_):
            leng = len(list_)
            if leng <= 1:
                return list_
            mid = leng // 2
            left = merge(list_[:mid])
            right = merge(list_[mid:])
            result = []
            while left and right:
                if left[0] > right[0]:
                    result.append(right.pop(0))
                    self.count += len(left)
                else:
                    result.append(left.pop(0))
            return result + left + right
        merge(nums)
        return self.count


if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs2([1,3,2,3,1]))