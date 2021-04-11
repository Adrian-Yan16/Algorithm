import heapq,sys


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if not n:
            return n
        ugly_l = [1]
        divisor2 = 0
        divisor3 = 0
        divisor5 = 0
        while len(ugly_l) < n:
            ugly = min(ugly_l[divisor2] * 2,ugly_l[divisor3] * 3,ugly_l[divisor5] * 5)
            ugly_l.append(ugly)
            if ugly % 2 == 0:
                divisor2 += 1
            if ugly % 3 == 0:
                divisor3 += 1
            if ugly % 5 == 0:
                divisor5 += 1
        return ugly_l[-1]

    # 堆
    def nthUglyNumber2(self, n: int) -> int:
        res = []
        ls = [1]
        # heapq.heapify(ls)
        for _ in range(n):
            cur = heapq.heappop(ls)
            res.append(cur)
            setls = set(ls)
            setcur = {cur * 2,cur * 3,cur * 5}
            diff = setcur.difference(setls)
            if diff:
                for item in diff:
                    heapq.heappush(ls,item)
        return res[-1]

    # 暴力
    def nthUglyNumber3(self, n: int) -> int:
        res = [1]
        def is_ugly_num(num):
            while num % 2 == 0:
                num //= 2
            while num % 3 == 0:
                num //= 3
            while num % 5 == 0:
                num //= 5
            return True if num == 1 else False
        for i in range(2,sys.maxsize):
            if len(res) == n:
                print(res)
                return res[-1]
            if is_ugly_num(i):
                res.append(i)




if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber3(10))