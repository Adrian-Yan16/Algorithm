# 空间复杂度O(n^2),空间复杂度O(n^2/2)
class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(2,numRows):
            res.append([1,1])
            temp = res[i - 1]
            for j in range(len(temp) - 1):
                res[i].insert(-1,temp[j] + temp[j + 1])
        return res


s = Solution()
print(s.generate(5))