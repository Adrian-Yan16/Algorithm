def is_happy(num):
    p = num
    q = get_next(num)
    while p and q and p != q:
        p = get_next(p)
        q = get_next(get_next(q))
        if p == 1 or q == 1:
            return num
    if not p or not q:
        return num
    else:
        return 0

def get_next(num):
    sum_ = 0
    while num:
        t = num % 10
        num = num // 10
        sum_ = sum_ + t ** 2
    return sum_

class Solution:
    def isHappy(self, n: int) -> bool:

        p = n
        q = self.get_next(n)
        while p and q and p != q:
            p = self.get_next(p)
            q = self.get_next(self.get_next(q))
            if p == 1 or q == 1:
                return True
        if not p or not q:
            return True
        else:
            return False

    def get_next(self,num):
        sum_ = 0
        while num:
            t = num % 10
            num = num // 10
            sum_ = sum_ + t ** 2
        return sum_

if __name__ == '__main__':
    sum_ = 1
    # for i in range(2,100001):
    #     if is_happy(i):
    #         sum_ += is_happy(i)
    # print(sum_)
    s = Solution()
    print(s.isHappy(1))