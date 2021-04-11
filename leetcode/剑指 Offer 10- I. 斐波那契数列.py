class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib2(self, n: int) -> int:
        if n <= 1:
            return n
        f1 = 0
        f2 = 1
        for _ in range(1,n):
            sum = f1 + f2
            f1 = f2
            f2 = sum
        return f2


if __name__ == '__main__':
    s = Solution()
    print(s.fib(6))
    print(s.fib2(6))

