triangle = [
    [2, 0, 0, 0],
    [3, 4, 0, 0],
    [6, 5, 7, 0],
    [4, 9, 8, 3]
]
# 以上三角形由一连串的数字构成，要求从顶点 2 开始走到最底下边的最短路径，
# 每次只能向当前节点下面的两个节点走，如 3 可以向 6 或 5 走，不能直接走到 7。
dict_ = {}
class Solution():
    def best_path_rec(self,i,j):
        row = len(triangle)
        if i >= row:
            return 0
        if str(i)+str(j) in dict_:
            return dict_[str(i)+str(j)]
        left_sum = triangle[i][j] + self.best_path_rec(i+1,j)
        right_sum = triangle[i][j] + self.best_path_rec(i+1,j+1)
        min_v = min(left_sum,right_sum)
        dict_[str(i)+str(j)] = min_v
        return min_v

    def best_path_dp(self,i,j):
        row = len(triangle)
        if i >= row:
            return 0
        mini = triangle[row - 1]
        for i in range(row - 2,-1,-1):
            for j in range(i+1):
                mini[j] = triangle[i][j] + min(mini[j],mini[j+1])
        return mini[0]




s = Solution()
print(s.best_path_rec(0,0))

print(s.best_path_dp(0,0))

