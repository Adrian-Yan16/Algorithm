class Solution:
    def constructArr(self, a):
        l = len(a)
        b = [1] * l
        for i in range(1,l):
            b[i] = b[i-1] * a[i-1]
        temp = 1
        for i in range(l-2,-1,-1):
            temp *= a[i+1]
            b[i] *= temp
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.constructArr([1,2,3,4,5]))