class Solution:
    def minArray(self, numbers) -> int:
        l = 0
        r = len(numbers) - 1
        while l < r:
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[l]


if __name__ == '__main__':
    s = Solution()
    print(s.minArray([3,4,5,1,2]))