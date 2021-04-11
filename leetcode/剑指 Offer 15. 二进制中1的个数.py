class Solution:
    # O(log2n)
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    # n & n-1 结果为将 n 最后一个 1 变为 0
    # n= 10101000,n-1=10100111,
    # n&n-1=10100000
    # O(m)
    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n-1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(11))
    print(s.hammingWeight2(11))
