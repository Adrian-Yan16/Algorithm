class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x and not n:
            return
        if not x:
            return 0
        if not n:
            return 1
        e = abs(n)
        res = 1
        while e:
            if e & 1 == 1:
                res *= x
            x *= x
            e >>= 1
        return res if n > 0 else 1/res


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(3,6))