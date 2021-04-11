import copy
class Solution:
    def solve_queen(self,n):
        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(board,row):
            if row == len(board):
                res.append(copy.deepcopy(board))
                return
            n = len(board)
            for col in range(n):
                # 判断当前位置放置皇后与已存在的是否冲突
                if not self.is_conflict(board,row,col):
                    continue
                board[row][col] = 'Q'
                backtrack(board,row + 1)
                board[row][col] = '.'

        backtrack(board,0)

    def is_conflict(self,board,row,col):
        n = len(board)
        # 判断列是否冲突
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # 判断左上和右上是否冲突
        j = col
        k = col
        for i in range(row - 1,-1,-1):
            j = j - 1
            if j >=0 and board[i][j] == 'Q':
                return False

        for i in range(row - 1,-1,-1):
            k = k + 1
            if k < n and board[i][k] == 'Q':
                return False
        return True


s = Solution()
print(s.solve_queen(4))

