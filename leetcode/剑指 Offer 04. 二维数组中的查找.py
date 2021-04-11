class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        l = len(matrix[0])
        k = len(matrix)
        for i in range(k):
            for j in range(-1,-l - 1,-1):
                temp = matrix[i][j]
                if temp == target:
                    return True
                elif temp > target:
                    if j == -l:
                        return False
                    continue
                else:
                    if i == k - 1:
                        return False
                    break
        return False


if __name__ == '__main__':
    matrix = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
    ]
    s = Solution()
    print(s.findNumberIn2DArray(matrix,31))


