import numpy as np

class Solution:
    def matrixScore(self, A) -> int:
        n,m = len(A),len(A[0])
        res = 2 ** (m-1) * n
        for i in range(1,m):
            ans = 0
            for j in range(n):
                if A[j][0]:
                    ans += A[j][i]
                else:
                    ans += 1 ^ A[j][i]
            # ans为0，1个数的最大值，如果0多要转为 1
            ans = max(ans,n - ans)
            # m-i-1为当前列的值
            res += ans * (1 << (m-i-1))
        return res

s = Solution()
print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
